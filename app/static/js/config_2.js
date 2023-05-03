const DATA_COUNT =  {
  type: 'bar',
  data: {
     labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
     datasets: [{
        label: "online tutorial subjects",
        data: [20, 40, 30, 35, 30, 20],
        backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'lightblue', 'gold'],
        borderColor: ['red', 'blue', 'fuchsia', 'green', 'navy', 'black'],
        borderWidth: 2,
     }],
  },
  options: {
     responsive: false,
  },
};