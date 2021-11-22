<template>
  <div>
    <div class="text-h2">
      SETTINGS
    </div>
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
    <div :style="{position: 'absolute', right: '200px', bottom: '100px'}">
      <apexcharts width="450" type="pie" :options="chartOptions" :series="series"></apexcharts>
    </div>
  </div>
</template>
<script>
import { onMounted,ref } from "vue";
import axios from "axios";
import VueApexCharts from 'vue3-apexcharts'
import {fetchKeystrokes} from 'src/utils/request.js';
import avertStore from 'src/avertStore';

export default {
  name: 'Chart',
  components:{
    apexcharts: VueApexCharts,
  },
  setup() {
    let series = ref([]);
    onMounted(() =>{
      fetchKeystrokes()
      conosole.log('onMounted')
    });
    
  },
  mounted(){
    console.log(avertStore)
  },
  data() {
    return {
      chartOptions: {
        chart: {
              width: 380,
              type: 'pie',
            },
            labels: ['Keystrokes', 'System Calls', 'Processes', 'Mouse Actions', 'Network Data'],
            responsive: [{
              breakpoint: 480,
              options: {
                chart: {
                  width: 200
                },
                legend: {
                  position: 'bottom'
                }
              }
            }],
            dataLabels: {
              style: {
                colors:[]
              }
            }
      },

      series: [44, 55, 41, 17, 15],
      // series,
      items: [
        { active: false, label: 'Record Keystrokes' }, 
        { active: false, label: 'Record Mouse' },
        { active: false, label: 'Record Screenshots' }, 
        { active: false, label: 'Record Processes' }, 
        { active: false, label: 'Record Window History' }, 
        { active: false, label: 'Record System Calls' },
        { active: false, label: 'Record Video' },
        { active: false, label: 'Record PCAP' },
      ],
      all: ref(false),
      options: ["Minutes", "Seconds"],
      text: ref(""),
    };
  },
  methods: {
    async toggleAll() {
      if (this.all) {
        this.items.forEach(element => {
          element.active = true;
        });
      } else {
        this.items.forEach(element => {
          element.active = false;
        });
      }
      this.toggle();
    },
    async toggle() {
      let post_data = {
        keystrokes: false, 
        mouse: false,
        screenshots: false, 
        processes: false, 
        window_history: false, 
        system_calls: false, 
        video: false, 
        pcap: false
      };
      let i = 0;
      for (var key in post_data) {
        if(!post_data.hasOwnProperty(key))
          continue;
        post_data[key] = this.items[i].active;
        i++;
      }

      console.log(post_data)

      const response = await axios.post(
        "http://localhost:5000/recording/",
        post_data
      );
      console.log(response);
    },
  },
};
</script>
<style lang=""></style>
