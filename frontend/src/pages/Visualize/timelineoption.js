export const chartOptions = {
    chart: {
      height: 350,
      type: 'line',
      zoom: {
        enabled: false
      },
      animations: {
        enabled: true
      }
    },
    stroke: {
      width: [5,5,4],
      curve: 'straight'
    },
    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    title: {
      text: 'Missing data (null values)'
    },
    xaxis: {
    }
  }