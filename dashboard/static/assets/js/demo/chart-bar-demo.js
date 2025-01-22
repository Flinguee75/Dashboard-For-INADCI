// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

async function loadCSV(filePath) {
  const response = await fetch(filePath);
  const csvText = await response.text();
  return parseCSV(csvText);
}

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

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myBarChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [], // Initialement vide
    datasets: [{
      label: "Pluviométrie (mm)",
      backgroundColor: "rgba(28, 200, 138, 0.5)",
      borderColor: "rgba(28, 200, 138, 0.5)",
      borderWidth: 1,
      data: [] // Données initiales vides
    }],
  },
  options: {
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        ticks: {
          maxTicksLimit: 12
        }
      }],
      yAxes: [{
        ticks: {
          callback: function(value) {
            return value + ' mm'; // Affiche les unités de pluviométrie
          }
        }
      }]
    },
    legend: {
      display: false
    },
    tooltips: {
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + ': ' + tooltipItem.yLabel + ' mm';
        }
      }
    }
  }
});

// Charger les données depuis le CSV
fetch('/static/assets/dataset/dataset_cleaned.csv')
  .then(response => response.text())
  .then(csvText => {
    const data = parseCSV(csvText); // Parse le fichier CSV
    const labels = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]; // Mois de l'année
    const filteredData = data.filter(row => row.nom_region === 'Comoé'); // Filtre pour la région Abidjan
    const values = filteredData.map(row => parseFloat(row.pluviometrie)); // Récupère les données de pluviométrie

    // Met à jour le graphique
    myBarChart.data.labels = labels;
    myBarChart.data.datasets[0].data = values;
    myBarChart.update();
  })
  .catch(error => console.error('Erreur lors du chargement des données CSV :', error));
