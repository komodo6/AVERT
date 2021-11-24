<template>
   <div id="chart">
        <apexchart type="line" height="350" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>



<script>
import { onMounted, ref } from "vue";
import VueApexCharts from 'vue3-apexcharts'
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
import {chartOptions} from "./timelineoption.js";

export default {
  name: 'Chart',
  components: {
    apexchart: VueApexCharts,
  },
  setup(){
      fetchMouseActionsTimeline();
      onMounted(() => {
          console.log(avertStore.state.mouseactions)
      });
    return{
        chartOptions
    }
  },
  data: function() {
    return {
      series: [{
            name: 'Peter',
            data: [5, 5, 10, 8, 7, 5, 4, null, null, null, 10, 10, 7, 8, 6, 9]
          }, {
            name: 'Johnny',
            data: [10, 15, null, 12, null, 10, 12, 15, null, null, 12, null, 14, null, null, null]
          }, {
            name: 'David',
            data: [null, null, null, null, 3, 4, 1, 3, 4,  6,  7,  9, 5, null, null, null]
          }]
    }    
  }
} 

</script>
