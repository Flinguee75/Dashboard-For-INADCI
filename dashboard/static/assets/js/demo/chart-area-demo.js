// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

async function loadCSV(filePath) {
  const response = await fetch(filePath);
  const csvText = await response.text();
  return parseCSV(csvText);
}

function parseCSV(csvText) {
  const rows = csvText.split("\n");
  const headers = rows[0].split(",");
  const data = rows.slice(1).map(row => {
      const values = row.split(",");
      return headers.reduce((acc, header, index) => {
          acc[header.trim()] = values[index].trim();
          return acc;
      }, {});
  });
  return data;
}

// Exemple d'utilisation
loadCSV('/static/assets/dataset/dataset_cleaned.csv').then(data => console.log(data));

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
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


// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [], // Initialement vide
    datasets: [{
      label: "Taux de rendement (%)",
      lineTension: 0.3,
      backgroundColor: "rgba(144, 238, 144, 0.05)", // Vert clair
      borderColor: "rgba(144, 238, 144, 1)", // Vert clair
      pointRadius: 3,
      pointBackgroundColor: "rgba(144, 238, 144, 1)", // Vert clair
      pointBorderColor: "rgba(144, 238, 144, 1)", // Vert clair
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(144, 238, 144, 1)", // Vert clair
      pointHoverBorderColor: "rgba(144, 238, 144, 1)", // Vert clair
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [] // Données initiales vides
    }],
  },
  options: {
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        ticks: {
          maxTicksLimit: 12
        }
      }],
      yAxes: [{
        ticks: {
          callback: function(value) {
            return value + 't/ha'; // Affiche le symbole de pourcentage
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
          return datasetLabel + ': ' + tooltipItem.yLabel + '%';
        }
      }
    }
  }
});

fetch('/static/assets/dataset/dataset_cleaned.csv')
  .then(response => response.text())
  .then(csvText => {
    const data = parseCSV(csvText); // Implémentez une fonction de parsing CSV
    const labels = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]; // Mois de l'année
    const filteredData = data.filter(row => row.nom_region === 'Abidjan'); // Filtre les données pour la région Abidjan
    const values = filteredData.map(row => parseFloat(row.rendement_moyen)); // Récupère les taux de rendement

    // Mettez à jour le graphique
    myLineChart.data.labels = labels;
    myLineChart.data.datasets[0].data = values;
    myLineChart.update();
  })
  .catch(error => console.error('Erreur lors du chargement des données CSV :', error));
