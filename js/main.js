// Startseite: Menü auf dem Handy, Reiter «Bereiche», Projektkarten mit Filter.
// Alles baut auf funktionierendem HTML auf: Ohne JavaScript bleibt die Seite vollständig.

// Ab hier läuft JavaScript: CSS darf Navigation und Bereiche einklappen.
document.documentElement.classList.replace("no-js", "js");

const PROJEKTE_URL = "data/projekte.json";

// Farbfeld pro Kategorie, bis echte Bilder vorliegen
const FELD_PRO_KATEGORIE = {
    "foto-video": "feld--ocker",
    "automatisierung-ki": "feld--oliv",
    studium: "feld--moos",
};

// ---------- Menü (Handy) ----------

function initialisiereMenue() {
    const kopf = document.querySelector(".kopfzeile");
    const knopf = kopf?.querySelector(".menue-knopf");
    if (!kopf || !knopf) {
        return;
    }

    const setzeOffen = (offen) => {
        kopf.classList.toggle("offen", offen);
        knopf.setAttribute("aria-expanded", String(offen));
    };

    knopf.addEventListener("click", () => {
        setzeOffen(knopf.getAttribute("aria-expanded") !== "true");
    });

    // Nach einem Klick auf einen Link schliesst das Menü wieder
    kopf.querySelector("nav").addEventListener("click", (ereignis) => {
        if (ereignis.target.closest("a")) {
            setzeOffen(false);
        }
    });

    document.addEventListener("keydown", (ereignis) => {
        if (ereignis.key === "Escape" && kopf.classList.contains("offen")) {
            setzeOffen(false);
            knopf.focus();
        }
    });
}

// ---------- Reiter «Bereiche» ----------

function initialisiereReiter() {
    const leiste = document.querySelector(".reiter-leiste");
    if (!leiste) {
        return;
    }
    const reiter = [...leiste.querySelectorAll('[role="tab"]')];

    const zeige = (index, fokus = false) => {
        reiter.forEach((r, i) => {
            const aktiv = i === index;
            r.setAttribute("aria-selected", String(aktiv));
            // Nur der aktive Reiter ist per Tab-Taste erreichbar, die anderen über Pfeiltasten
            r.tabIndex = aktiv ? 0 : -1;
            document.getElementById(r.getAttribute("aria-controls")).hidden = !aktiv;
        });
        if (fokus) {
            reiter[index].focus();
        }
    };

    const aktuell = () => reiter.findIndex((r) => r.getAttribute("aria-selected") === "true");
    // Modulo mit Ausgleich, damit -1 auf den letzten Reiter springt
    const verschiebe = (schritt) => (aktuell() + schritt + reiter.length) % reiter.length;

    leiste.addEventListener("click", (ereignis) => {
        const r = ereignis.target.closest('[role="tab"]');
        if (r) {
            zeige(reiter.indexOf(r));
        }
    });

    leiste.addEventListener("keydown", (ereignis) => {
        if (ereignis.key === "ArrowRight") {
            zeige(verschiebe(1), true);
        } else if (ereignis.key === "ArrowLeft") {
            zeige(verschiebe(-1), true);
        }
    });

    document.querySelectorAll(".reiter-pfeile [data-schritt]").forEach((knopf) => {
        knopf.addEventListener("click", () => zeige(verschiebe(Number(knopf.dataset.schritt))));
    });

    zeige(0);
}

// ---------- Projekte ----------

async function ladeProjekte() {
    const antwort = await fetch(PROJEKTE_URL);
    if (!antwort.ok) {
        throw new Error(`Projekte konnten nicht geladen werden (${antwort.status})`);
    }
    return antwort.json();
}

function element(tag, klasse, text) {
    const el = document.createElement(tag);
    if (klasse) {
        el.className = klasse;
    }
    if (text) {
        el.textContent = text;
    }
    return el;
}

// Pfeil aus dem SVG-Symbol im HTML wiederverwenden
function pfeil() {
    const ns = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(ns, "svg");
    svg.setAttribute("aria-hidden", "true");
    const use = document.createElementNS(ns, "use");
    use.setAttribute("href", "#pfeil");
    svg.append(use);
    return svg;
}

// Baut eine Karte. textContent statt innerHTML, damit Text aus der
// JSON-Datei nie als HTML ausgeführt wird.
function erstelleKarte(projekt, kategorieLabel) {
    const karte = element("article", "karte");
    karte.dataset.kategorie = projekt.kategorie;

    const feld = element("div", `feld ${FELD_PRO_KATEGORIE[projekt.kategorie] ?? ""}`);
    feld.append(element("span", "notiz", `${kategorieLabel} · Bild folgt`));

    const titel = element("h3");
    if (projekt.link) {
        const link = element("a", "", projekt.titel);
        link.href = projekt.link;
        titel.append(link);
    } else {
        titel.textContent = projekt.titel;
    }

    const kopfText = element("div");
    kopfText.append(titel, element("p", "projekt-meta", projekt.meta));

    const kopf = element("div", "karte-kopf");
    kopf.append(kopfText);

    if (projekt.link) {
        // Zweiter Link zur selben Seite: für Screenreader ausgeblendet, der Titel genügt
        const mehr = element("a", "ansehen", "Ansehen");
        mehr.href = projekt.link;
        mehr.setAttribute("aria-hidden", "true");
        mehr.tabIndex = -1;
        mehr.append(pfeil());
        kopf.append(mehr);
    }

    karte.append(
        feld,
        kopf,
        element("p", "karte-text", projekt.text),
        element("p", "projekt-tags", projekt.tags.join(" · "))
    );
    return karte;
}

function erstelleFilterKnopf(id, label, aktiv) {
    const knopf = element("button", "", label);
    knopf.type = "button";
    knopf.dataset.filter = id;
    // aria-pressed sagt Screenreadern, welcher Filter gerade gilt
    knopf.setAttribute("aria-pressed", String(aktiv));
    return knopf;
}

function filtere(liste, filterLeiste, id) {
    for (const karte of liste.children) {
        karte.hidden = id !== "alle" && karte.dataset.kategorie !== id;
    }
    for (const knopf of filterLeiste.children) {
        knopf.setAttribute("aria-pressed", String(knopf.dataset.filter === id));
    }
}

async function zeigeProjekte() {
    const liste = document.getElementById("projekt-liste");
    const filterLeiste = document.getElementById("projekt-filter");
    if (!liste || !filterLeiste) {
        return;
    }

    let daten;
    try {
        daten = await ladeProjekte();
    } catch (fehler) {
        console.warn(fehler);
        return;
    }

    const labels = new Map(daten.kategorien.map((k) => [k.id, k.label]));

    liste.replaceChildren(
        ...daten.projekte.map((p) => erstelleKarte(p, labels.get(p.kategorie)))
    );

    filterLeiste.replaceChildren(
        erstelleFilterKnopf("alle", `Alle ${daten.projekte.length}`, true),
        ...daten.kategorien.map((k) => erstelleFilterKnopf(k.id, k.label, false))
    );
    filterLeiste.hidden = false;

    // Ein Listener für alle Knöpfe (Event Delegation)
    filterLeiste.addEventListener("click", (ereignis) => {
        const knopf = ereignis.target.closest("button[data-filter]");
        if (knopf) {
            filtere(liste, filterLeiste, knopf.dataset.filter);
        }
    });
}

initialisiereMenue();
initialisiereReiter();
zeigeProjekte();
