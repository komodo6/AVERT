<template>
  <div class="viz-container">
    <div class="row">
      <div class="col-12">
        <div class="text-h3">Visualization</div>
        <div class="col-12">
          <div>
            <q-form>
              <div class="row">
                <div class="col-5">
                  <div class="row">
                    <div class="col">
                      <div class="text-subtitle1">Select Graph Type</div>
                    </div>
                  </div>
                  <div class="q-pa-md" style="max-width: 300px">
                    <div class="q-gutter-md">
                      <q-select filled v-model="model" :options="options" label="Pick Graph Type" />
                  <!-- <div class="row">
                    <div class="col-2.5">
                      <q-radio> Timeline </q-radio>
                    </div>
                    <div class="col-2.5">
                      <q-radio> Bar Graph </q-radio>
                    </div>
                    <div class="col-2.5">
                      <q-radio> Pie Chart </q-radio>
                    </div>
                    <div class="col-2.5">
                      <q-radio> CPU Usage </q-radio>
                    </div> -->
                    </div>
                  </div>
                </div>
                <div class="col-7">
                  <div class="row">
                    <div class="col">
                      <div class="text-subtitle1">Enter Time Frame</div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-4">
                      <div clas="start-date">
                        <label> Start Date</label>
                        <input v-model="startTime" type="datetime-local" step="0.001" />
                      </div>
                    </div>
                    <div class="col-4">
                      <div clas="end-date">
                        <label> End Date</label>
                        <input v-model="endTime" type="datetime-local" step="0.001"/>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-5">
                  <div class="row">
                    <div class="col-3">
                      <div class="q-pa-md">
                        <div class="q-gutter-sm">  
                          <q-checkbox v-model="selection" val="processes" label="Processes" />
                          <q-checkbox v-model="selection" val="systemCalls" label="System Calls" />
                          <q-checkbox v-model="selection" val="videos" label="Videos" />
                          <q-checkbox v-model="selection" val="mouseActions" label="Mouse Actions" />
                          <q-btn size="md" color="grey-9" label="Select All"  @click="selectAll"></q-btn>
                        </div>
                      </div>  
                      <!-- <q-checkbox> Select All </q-checkbox>
                      <q-checkbox> Mouse Movements </q-checkbox>
                      <q-checkbox> PCAP </q-checkbox> -->
                    </div>
                    <div class="col-3">
                    <div class="q-pa-md">
                      <div class="q-gutter-sm">
                        <q-checkbox v-model="selection" val="screenShots" label="Screenshots" />
                        <q-checkbox v-model="selection" val="windowHistory" label="Window History" />
                        <q-checkbox v-model="selection" val="keyStrokes" label="Keystrokes" />
                        <q-checkbox v-model="selection" val="networkData" label="Network Data" />
                        <q-btn size="md" color="grey-9" label="Unselect Al"  @click="unselectAll"></q-btn>

                      </div>
                    </div>  
                      <!-- <q-checkbox> Screenshots </q-checkbox>
                      <q-checkbox> Window Histories </q-checkbox>
                      <q-checkbox> Keystrokes </q-checkbox> -->
                    </div>
                  </div>
                </div>
                <div class="col-6">
                  <div v-if="model === 'Timeline'">
                  <div class="row">
                    
                    <div class="col">
                      <div class="text-subtitle1">Select Graph Interval</div>
                    
                    </div>
                  </div>
                  <!-- <div class="row">
                    <div class="col-2">
                      <div class="q-pa-md">
                        <div class="q-gutter-sm">
                          <q-radio v-model="interval" val="day" label="By Day" />
                        </div>
                      </div>   
                    </div>
                  <div class="row">
                    <div class="col-2">
                      <div class="q-pa-md">
                        <div class="q-gutter-sm">
                          <q-radio v-model="interval" val="hour" label="By Hour" />
                        </div>
                      </div>   
                    </div>
                  </div>
                    <div class="row">
                    <div class="col-2">
                      <div class="q-pa-md">
                        <div class="q-gutter-sm">
                          <q-radio v-model="interval" val="minute" label="By Minutes" />
                        </div>
                      </div>   
                    </div>
                    </div>
                    <div class="row">
                    <div class="col-2">
                      <div class="q-pa-md">
                        <div class="q-gutter-sm">
                          <q-radio v-model="interval" val="second" label="By Seconds" />
                        </div>
                      </div>   
                    </div>
                  </div> -->
                  <!-- </div> -->
                  </div>
                  <div class="row">
                    <div class="col-5">
                      <q-btn @click="generateGraph" size="lg" color="grey-9">
                        Generate Graph
                      </q-btn>
                    </div>
                  </div>
                </div>
              </div>
            </q-form>
            <div v-if="graphToShow === 'Timeline' ">
              <TimeLine :startTime="startTime" :endTime="endTime" :selectedArtifacts="selection"/>
            </div>
            <div v-if="graphToShow === 'Bar Graph'">
              <BarChart/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  
</template>
<script>
import { ref } from "vue";
import TimeLine from "./Timelinechart.vue";
import BarChart from "./BarChart.vue";

export default {
  components:{
    TimeLine,
    BarChart
  },
  data() {
    return {
      startTime: '2021-11-23 02:12:36.200',
      endTime: '2021-11-23 02:12:37.100',
      graphToShow: ref(''),
      model: ref(null),
      options: [ 'Bar Graph', 'Timeline'],
      selection: [],
      optionsa: ['mouseActions', 'networkData', 'screenShots', 'windowHistory', 'videos', 'processes', 'keyStrokes', 'systemCalls' ],
      //interval: ref(null),
      interval: ref(null),
    }
  },
      
      
      //sa,
      // sc,
      // mm,
      // wh,
      // pc,
      // ks,

      // val: ref(true),
      // int: ref(true),

  methods:{
    selectAll(){
      this.selection = this.optionsa;
      },

    unselectAll(){
      this.selection = []
    },
     generateGraph(){
       
      this.graphToShow = this.model;
    }
  },
}


</script>

<style scoped>
.viz-container {
  margin: 2em;
}
</style>
