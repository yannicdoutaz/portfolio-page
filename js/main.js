// Projekte: Karten und Filter aus data/projekte.json erzeugen.
// Scheitert das Laden, bleiben die statischen Karten im HTML stehen.

const PROJEKTE_URL = "data/projekte.json";

async function ladeProjekte() {
    const antwort = await fetch(PROJEKTE_URL);
    if (!antwort.ok) {
        throw new Error(`Projekte konnten nicht geladen werden (${antwort.status})`);
    }
    return antwort.json();
}

// Baut eine Karte. textContent statt innerHTML, damit Text aus der
// JSON-Datei nie als HTML ausgeführt wird.
function erstelleKarte(projekt, kategorieLabel) {
    const karte = document.createElement("article");
    karte.className = "card";
    karte.dataset.kategorie = projekt.kategorie;

    const titel = document.createElement("h3");
    if (projekt.link) {
        const link = document.createElement("a");
        link.href = projekt.link;
        link.textContent = projekt.titel;
        titel.append(link);
    } else {
        titel.textContent = projekt.titel;
    }

    const kategorie = document.createElement("p");
    kategorie.className = "projekt-kategorie";
    kategorie.textContent = kategorieLabel;

    const meta = document.createElement("p");
    meta.className = "projekt-meta";
    meta.textContent = projekt.meta;

    const text = document.createElement("p");
    text.textContent = projekt.text;

    const tags = document.createElement("ul");
    tags.className = "projekt-tags";
    for (const tag of projekt.tags) {
        const eintrag = document.createElement("li");
        eintrag.textContent = tag;
        tags.append(eintrag);
    }

    karte.append(kategorie, titel, meta, text, tags);

    if (projekt.link) {
        const mehr = document.createElement("p");
        const link = document.createElement("a");
        link.href = projekt.link;
        link.textContent = "Projekt ansehen";
        mehr.append(link);
        karte.append(mehr);
    }

    return karte;
}

function erstelleFilterKnopf(id, label, aktiv) {
    const knopf = document.createElement("button");
    knopf.type = "button";
    knopf.dataset.filter = id;
    knopf.textContent = label;
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
        erstelleFilterKnopf("alle", "Alle", true),
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

zeigeProjekte();
