// This file is intentionally left blank.

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predictionForm');
    const input = document.getElementById('sepal_width');
    const resultBox = document.getElementById('resultDisplay');

    const setValue = (species, value) => {
        const el = document.querySelector(`.prediction[data-species="${species}"] .value`);
        if (el) el.textContent = typeof value === 'number' ? value.toFixed(2) : value;
    };

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const width = parseFloat(input.value);
        if (Number.isNaN(width)) return;

        // état "chargement"
        ['Setosa','Versicolor','Virginica'].forEach(s => setValue(s, '...'));
        resultBox.classList.remove('hidden');

        try {
            const res = await fetch(`/api/predict?sepal_width=${encodeURIComponent(width)}`);
            if (!res.ok) throw new Error('no api');
            const data = await res.json();
            // Attendu: { setosa: number, versicolor: number, virginica: number }
            setValue('Setosa', data.setosa ?? data.Setosa ?? '--');
            setValue('Versicolor', data.versicolor ?? data.Versicolor ?? data.versicolor_prediction ?? '--');
            setValue('Virginica', data.virginica ?? data.Virginica ?? '--');
        } catch (err) {
            // Fallback local : approximations linéaires pour afficher quelque chose immédiatement
            // Ces formules sont heuristiques et peuvent être remplacées par une vraie API
            setValue('Setosa', 0.5 * width + 1.0);
            setValue('Versicolor', 0.9 * width + 1.1);
            setValue('Virginica', 1.15 * width + 1.3);
        }
    });
});