// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Fonction pour charger et parser un fichier CSV
async function loadCSV(filePath) {
  const response = await fetch(filePath);
  const csvText = await response.text();
  return parseCSV(csvText);
}

// Fonction pour parser le CSV
function parseCSV(csvText) {
  const rows = csvText.split("\n").filter(row => row.trim() !== ""); // Supprime les lignes vides
  const headers = rows[0].split(","); // Première ligne pour les en-têtes
  return rows.slice(1).map(row => {
    const values = row.split(",");
    return headers.reduce((acc, header, index) => {
      acc[header.trim()] = values[index].trim();
      return acc;
    }, {});
  });
}

// Charger les données et configurer le graphe
loadCSV('/static/assets/dataset/dataset_cleaned.csv').then(data => {
  // Filtrer les données pour la région Abidjan
  const filteredData = data.filter(row => row.nom_region === 'Abidjan');

  // Calculer les occurrences des espèces
  const speciesCount = {};
  filteredData.forEach(row => {
    const espece = row.nom_espece;
    speciesCount[espece] = (speciesCount[espece] || 0) + 1;
  });

  // Préparer les données pour le graphe
  const labels = Object.keys(speciesCount);
  const values = Object.values(speciesCount);
  const colors = labels.map(() => `#${Math.floor(Math.random() * 16777215).toString(16)}`);

  // Configurer le graphe donut
  var ctx = document.getElementById("myPieChart");
  var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: labels,
      datasets: [{
        data: values,
        backgroundColor: colors,
        hoverBackgroundColor: colors.map(color => darkenColor(color, 20)),
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      }],
    },
    options: {
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        caretPadding: 10,
      },
      legend: {
        display: true,
        position: 'bottom',
      },
      cutoutPercentage: 80,
    },
  });
}).catch(error => {
  console.error('Erreur lors du chargement des données CSV :', error);
});

// Fonction pour assombrir les couleurs (optionnel)
function darkenColor(color, percent) {
  const num = parseInt(color.slice(1), 16),
        amt = Math.round(2.55 * percent),
        R = (num >> 16) + amt,
        G = ((num >> 8) & 0x00FF) + amt,
        B = (num & 0x0000FF) + amt;
  return `#${(0x1000000 + (R < 255 ? R < 1 ? 0 : R : 255) * 0x10000 + 
                  (G < 255 ? G < 1 ? 0 : G : 255) * 0x100 + 
                  (B < 255 ? B < 1 ? 0 : B : 255)).toString(16).slice(1)}`;
}
