<template>
  <div id="chart">
    <apexchart
      type="line"
      height="350"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>



<script>
import { onMounted, ref } from "vue";
import VueApexCharts from "vue3-apexcharts";
import avertStore from "src/avertStore";
import {
  fetchKeystrokes,
  fetchMouseActionsTimeline,
  fetchScreenshots,
  fetchProcesses,
  fetchWindowHistory,
  fetchSystemCalls,
  fetchVideos,
} from "src/utils/request.js";
import axios from 'axios'; 
// import {chartOptions} from "./timelineoption.js";

export default {
  name: "Chart",
  components: {
    apexchart: VueApexCharts,
  },
  async created(){

    const maTimeline = await axios.post("http://localhost:5000/mouseactions/timeline", {
      start: 'start',
      end: 'end',
    })
    console.log('maTimeline' + JSON.stringify(maTimeline) )
    console.log(maTimeline['data']['r_intervals'])




    this.series= [
        {
          name: "Mouse Action",
          data:maTimeline['data']['r_intervals'],
        }
      ];


    this.chartOptions = {
        chart: {
          height: 350,
          type: "line",
          zoom: {
            enabled: false,
          },
          animations: {
            enabled: true,
          },
        },
        stroke: {
          width: [5, 5, 4],
          curve: "straight",
        },
        title: {
          text: "Missing data (null values)",
        },
        xaxis: {
            categories:maTimeline['data']['r_times']
        },
      }; 
  },
  data(){
    return{
        series: [
        {
          name: "Mouse Action",
          data:[],
        }
      ],
      chartOptions : {
        chart: {
          height: 350,
          type: "line",
          zoom: {
            enabled: false,
          },
          animations: {
            enabled: true,
          },
        },
        stroke: {
          width: [5, 5, 4],
          curve: "straight",
        },
        title: {
          text: "Missing data (null values)",
        },
        xaxis: {
            categories:[]
        },
      } 
    }
  }
  // setup() {
  //   let series = ref([]);
  //   series.value = [
  //       {
  //         name: "Mouse Action",
  //         data:[],
  //       }
  //     ];



  //   let chartOptions = ref({});

  //   chartOptions.value = {
  //       chart: {
  //         height: 350,
  //         type: "line",
  //         zoom: {
  //           enabled: false,
  //         },
  //         animations: {
  //           enabled: true,
  //         },
  //       },
  //       stroke: {
  //         width: [5, 5, 4],
  //         curve: "straight",
  //       },
  //       labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
  //       title: {
  //         text: "Missing data (null values)",
  //       },
  //       xaxis: {
  //           categories:[]
  //       },
  //     };



    
  //   onMounted(() => {
  //     console.log(avertStore.state.mouseActionsTimeline);
  //     fetchMouseActionsTimeline();
  //     chartOptions.value = {
  //       chart: {
  //         height: 350,
  //         type: "line",
  //         zoom: {
  //           enabled: false,
  //         },
  //         animations: {
  //           enabled: true,
  //         },
  //       },
  //       stroke: {
  //         width: [5, 5, 4],
  //         curve: "straight",
  //       },
  //       title: {
  //         text: "Missing data (null values)",
  //       },
  //       xaxis: {
  //           categories:avertStore.state.mouseActionsTimeline['r_times']
  //       },
  //     };

  //     series.value = [
  //       {
  //         name: "Mouse Action",
  //         data:avertStore.state.mouseActionsTimeline['r_intervals'],
  //       }
  //     ];
  //   });
  //   return {
  //     chartOptions,
  //     series,
  //   };
  // },
};
</script>
