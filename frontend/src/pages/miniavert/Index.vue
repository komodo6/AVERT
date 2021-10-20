<template>
  <div class="">
    <div class="row items-center justify-center">
      <div class="col-6">
        <div>
          <q-list>
            <q-item>
              <q-item-section>
                <q-toggle v-model="opt1"> replace me </q-toggle>

                <q-toggle v-model="opt2"> replace me </q-toggle>
                <q-toggle v-model="opt3"> replace me </q-toggle>
              </q-item-section>
            </q-item>
          </q-list>
        </div>
      </div>
    </div>
    <div class="row items-center justify-center q-ma-md">
      <div class="col-6">
        <div>
          <q-btn-group>
            <q-btn @click="startRecording"> Start </q-btn>
            <q-btn> Not Sure what goes here </q-btn>
            <q-btn @click="startRecording"> Stop </q-btn>
          </q-btn-group>
        </div>
      </div>
    </div>

    <div class="row items-center justify-center q-ma-md">
      <div class="col-6">
        <div>
          <q-btn @click="captureScreenshot"> capture screenshot </q-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

import axios from "axios";
export default {
  setup() {
    let opt1 = ref(false);
    let opt2 = ref(false);
    let opt3 = ref(false);
    const startRecording = () => {
      console.log("recording starting");
    };
    const stopRecording = () => {
      console.log("recording stopping");
    };

    const captureScreenshot = async () => {
      axios.get("http://localhost:5000/screenshots/capture");
    };

    return {
      opt1,
      opt2,
      opt3,
      captureScreenshot,
      stopRecording,
      startRecording,
    };
  },
};
</script>

<style scoped>
.q-btn {
  background-color: dimgray;
}
</style>
