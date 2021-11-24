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
  fetchKeystrokesCount,
  fetchMouseActionsCount,
  fetchScreenshotsCount,
  fetchProcessesCount,
  fetchWindowHistoryCount,
  fetchSystemCallsCount,
  fetchVideosCount,
} from "src/utils/request.js";
import { chartOptions } from "./barchartoption";
export default {
  name: "Chart",
  components: {
    apexchart: VueApexCharts,
  },
  setup() {
    let series = ref([]);
    fetchKeystrokesCount();
    fetchMouseActionsCount();
    fetchScreenshotsCount();
    fetchProcessesCount();
    fetchWindowHistoryCount();
    fetchSystemCallsCount();
    fetchVideosCount();
    onMounted(() => {
      series.value = [
        {
          name: "Inflation",
          data: [
            avertStore.state.keystrokes,
            avertStore.state.systemcalls,
            avertStore.state.processes,
            avertStore.state.mouseactions,
            0,
            avertStore.state.screenshots,
            avertStore.state.windowhistory,
            avertStore.state.videos,
          ],
        },
      ];
    });

    return {
      series,
      chartOptions,
    };
  },
};
</script>
