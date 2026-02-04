document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("predictionForm");
  const input = document.getElementById("sepal_width");
  const resultBox = document.getElementById("resultDisplay");

  const setValue = (species, value) => {
    const el = document.querySelector(`.prediction[data-species="${species}"] .value`);
    if (!el) return;

    if (typeof value === "number" && Number.isFinite(value)) {
      el.textContent = value.toFixed(2);
    } else {
      el.textContent = value ?? "--";
    }
  };

  const setLoading = (isLoading) => {
    const btn = form.querySelector('button[type="submit"]');
    if (!btn) return;
    btn.disabled = isLoading;
    btn.textContent = isLoading ? "PRÉDICTION..." : "PRÉDIRE";
  };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const width = parseFloat(input.value);
    if (!Number.isFinite(width) || width < 0) return;

    // UI: loading
    ["Setosa", "Versicolor", "Virginica"].forEach((s) => setValue(s, "..."));
    resultBox.classList.remove("hidden");
    setLoading(true);

    try {
      const res = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sepal_width: width }),
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || "Erreur API");

      const preds = data.predictions_by_species || {};

      setValue("Setosa", preds.setosa);
      setValue("Versicolor", preds.versicolor);
      setValue("Virginica", preds.virginica);
    } catch (err) {
      setValue("Setosa", "--");
      setValue("Versicolor", "--");
      setValue("Virginica", "--");
      console.error(err);
      alert("Impossible de contacter l’API Flask. Vérifie que le serveur tourne bien.");
    } finally {
      setLoading(false);
    }
  });
});
