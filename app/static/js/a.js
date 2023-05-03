<script>
        require([
            "esri/Map",
            "esri/views/MapView",
            "esri/layers/FeatureLayer",
            "esri/PopupTemplate",
            "esri/popup/content/CustomContent",
        ], (Map, MapView, FeatureLayer, PopupTemplate, CustomContent) => {
            // setup the map
            const map = new Map({
                basemap: "hybrid",
            });
            const view = new MapView({
                container: "viewDiv",
                map: map,
                center: [-81.31557659295213, 48.12557766494745],
                zoom: 6,
                popup: {
                    dockEnabled: true,
                    dockOptions: {
                        buttonEnabled: false,
                        breakpoint: false,
                    },
                },
            });
            const featureLayer = new FeatureLayer({
                url: "https://services.arcgis.com/6iGx1Dq91oKtcE7x/ArcGIS/rest/services/Census_Data/FeatureServer/2",
                outFields: ["*"],
            });
            let customContent = new CustomContent({
                outFields: ["*"],
                creator: (event) => {
                    console.log("in custom content");
                    // Call method to create chart with your own information.
                    // Use event.graphic value to reference current feature.
                    let canvas = createChart();
                    //const div = document.getElementById("chart-div");
                    let div = document.createElement("div");
                    div.appendChild(canvas);
                    // Return the div element containing the chart.
                    return div;
                },
            });
            // Create the PopupTemplate and reference custom content element.
            const template = new PopupTemplate({
                outFields: ["*"],
                title: "Chart",
                content: [customContent],
            });
            featureLayer.popupTemplate = template;
            map.add(featureLayer);
            // Create the custom chart using ChartJS library.
            // Example here: https://tobiasahlin.com/blog/chartjs-charts-to-get-you-started/#2-line-chart
            let lineChart;

            function createChart() {
                let canvas = document.createElement("canvas");
                canvas.style.width = "100%";
                canvas.style.height = "100%";
                canvas.width = 416;
                canvas.height = 208;
                const ctx = canvas.getContext("2d");
                const config = {
                    type: "line",
                    data: {
                        labels: ["val1", "val2", "val3", "val4", "val5"],
                        datasets: [{
                            data: [10, 50, 100, 150, 200],
                            label: "Values",
                            borderColor: "#3e95cd",
                            fill: false,
                        }, ],
                    },
                };
                console.log("creating chart");
                lineChart = new Chart(canvas, config);
                return canvas;
            }
        });
    </script>