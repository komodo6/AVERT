<template>
  <div>
    <div class="text-h2">SETTINGS</div>
    <div class="row">
      <div class="col">
        <div class="row">
          <div class="col">
            <q-list bordered>
              <q-item>
                <q-item-section>
                  <q-item-label>Toggle All</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="all"
                    v-on:click="toggleAll()"
                  />
                </q-item-section>
              </q-item>
              <q-item v-for="item in items" :key="item.label">
                <q-item-section>
                  <q-item-label>{{ item.label }}</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="item.active"
                    v-on:click="toggle()"
                  />
                </q-item-section>
              </q-item>
            </q-list>
          </div>
          <div class="col">
            <q-list bordered>
              <q-item>
                <q-item-section>
                  <q-item-label>PCAP Creation Interval</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-input color="primary" v-model="text" />
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Idle Recording Threshold</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-input color="primary" v-model="text" />
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Process Capture Interval</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-input color="primary" v-model="text" />
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="row">
          <div class="col">
            <q-list bordered>
              <q-item>
                <q-item-section>
                  <q-item-label>Frame Rate</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Resolution</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Video Length</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-input color="primary" v-model="text" />
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
            </q-list>
          </div>
          <div class="col">
            <q-list bordered>
              <q-item>
                <q-item-section>
                  <q-item-label>File Type</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </div>
      </div>
    </div>
    <div :style="{ position: 'absolute', right: '200px', bottom: '100px' }">
      <apexcharts
        width="550"
        type="pie"
        :options="chartOptions"
        :series="[avertStore.state.keystrokes, avertStore.state.systemcalls, avertStore.state.processes, avertStore.state.mouseactions, 0, avertStore.state.screenshots, avertStore.state.windowhistory, avertStore.state.videos, 10]"
      ></apexcharts>
    </div>
  </div>
</template>
<script>
import { onMounted, ref } from "vue";
import axios from "axios";
import VueApexCharts from "vue3-apexcharts";
import { fetchKeystrokes, fetchMouseActions, fetchScreenshots, fetchProcesses, fetchWindowHistory, fetchSystemCalls, fetchVideos} from "src/utils/request.js";
import avertStore from "src/avertStore";

export default {
  name: "Chart",
  components: {
    apexcharts: VueApexCharts,
  },
  setup() {
    let chartOptions = {
      chart: {
        width: 550,
        type: "pie",
      },
      labels: [
        "Keystrokes",
        "System Calls",
        "Processes",
        "Mouse Actions",
        "Network Data",
        "Screenshots",
        "Window History",
        "Video",
        "Remaining Storage"
      ],
      responsive: [
        {
          breakpoint: 480,
          options: {
            chart: {
              width: 200,
            },
            legend: {
              position: "bottom",
            },
          },
        },
      ],
      dataLabels: {
        style: {
          colors: [],
        },
      },
    };

    let items = [
      { active: false, label: "Record Keystrokes" },
      { active: false, label: "Record Mouse" },
      { active: false, label: "Record Screenshots" },
      { active: false, label: "Record Processes" },
      { active: false, label: "Record Window History" },
      { active: false, label: "Record System Calls" },
      { active: false, label: "Record Video" },
      { active: false, label: "Record PCAP" },
    ];
    let all = ref(false);
    let options = ["Minutes", "Seconds"]
    let text = ref("");

    onMounted(() => {
      fetchKeystrokes();
      fetchMouseActions();
      fetchScreenshots();
      fetchProcesses();
      fetchWindowHistory();
      fetchSystemCalls();
      fetchVideos();
      console.log("onMounted");
    });


    const toggleAll = async () => {
      if (this.all) {
        this.items.forEach((element) => {
          element.active = true;
        });
      } else {
        this.items.forEach((element) => {
          element.active = false;
        });
      }
      this.toggle();
    };

    const toggle = async () => {
      let post_data = {
        keystrokes: false,
        mouse: false,
        screenshots: false,
        processes: false,
        window_history: false,
        system_calls: false,
        video: false,
        pcap: false,
      };
      let i = 0;
      for (var key in post_data) {
        if (!post_data.hasOwnProperty(key)) continue;
        post_data[key] = this.items[i].active;
        i++;
      }

      console.log(post_data);

      const response = await axios.post(
        "http://localhost:5000/recording/",
        post_data
      );
      console.log(response);
    };

    return {
      toggleAll,
      toggle,
      items,
      all,
      options,
      text,
      chartOptions,
      avertStore,
    };
  },
};
</script>
<style lang=""></style>
