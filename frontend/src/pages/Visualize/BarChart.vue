<template>
  <div id="chart">
    <apexchart
      type="bar"
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
  fetchMouseActions,
  fetchScreenshots,
  fetchProcesses,
  fetchWindowHistory,
  fetchSystemCalls,
  fetchVideos,
} from "src/utils/request.js";
import { chartOptions } from "./barchartoption";
import axios from 'axios'
export default {
  name: "Chart",
  components: {
    apexchart: VueApexCharts,
  },
  async created() {
    // let series = ref([]);
    console.log( 'Chart Options: ' + JSON.stringify(chartOptions))

    const ks = await axios.get("http://localhost:5000/keystrokes/count");
    // await fetchKeystrokes();
    console.log(ks.data)
    const ma = await axios.get("http://localhost:5000/mouseactions/count");
    console.log(ma.data)
    // await fetchScreenshots();
    const ps = await axios.get("http://localhost:5000/processes/count");
    console.log(ps.data)
    // await fetchProcesses();

    const wh = await axios.get("http://localhost:5000/windows/count");
    console.log(wh.data)
    // await fetchWindowHistory();
    const sc = await axios.get("http://localhost:5000/systemcalls/count");
    console.log(sc.data)
    // await fetchSystemCalls();

    // const vi = await axios.get("http://localhost:5000'/videos/count");
    // console.log(vi.data)
    // await fetchVideos();
      this.series = [
        {
          name: "BarChart",
          data: [
            ks.data,
            sc.data,
            ps.data,
            ma.data,
            0,
            sc.data,
            wh.data,
            0,
          ],
        },
      ];

  },
  data(){
    return{
      series:[
        {
          name: "Inflation",
          data: [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
          ],
        },
      ],
      chartOptions: chartOptions
    }
  }
};
</script>
