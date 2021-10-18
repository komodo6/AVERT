<!--
<template>
  <div class="q-pa-md">
    <div class="q-gutter-sm">
      <q-checkbox v-model="val" />
    </div>

    <div class="q-px-sm">
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
export default {
  setup () {
    return {
      val: ref(true)
    }
  }
}
</script>
-->


<template>

  <div style="width:1000px;">

  <div style="width:500px; float:left;">
  <div class="q-pa-md">
    <div class="q-gutter-sm">
      <h1 style="font-size:30px;padding-left:5px;">Visualization</h1>
      <p style="padding-left:20px; font-size:17px;"> Select type of graph</p>
      <q-radio  val="tl" label="Timeline" v-model="val"/>
      <q-radio  val="bg" label="Bar Graph" v-model="val" />
      <q-radio  val="pc" label="Pie Chart" v-model="val"/>
      <q-radio  val="cpu" label="CPU Usage" v-model="val" />
      <br>
      <br>
      
    </div>
  </div>
   <div class="q-pa-md">
    <div class="q-gutter-sm">
      <p style="padding-left:20px; font-size:17px;"> Select data to include</p>
      <q-checkbox style="padding-right:60px;" label="Select All" v-model="val" />
      <q-checkbox  label="Screenshots" v-model="val"/><br>
      <q-checkbox  label="Mouse Movements" v-model="val" />
      <q-checkbox  label="Window Histories" v-model="val" /><br>
      <q-checkbox style="padding-right:84px;" label="PCAP" v-model="val"/>
      <q-checkbox  label="Keystrokes" v-model="val"/><br>
    </div>
   </div>  

  </div>
  <div style="width:500px; float:right;padding-top:133px;">
    <div style="width:400px;">
    <p style="font-size:17px;">Enter Time Frame</p>

  <div style="width:300px; float:left;"> 
    <div style="clear: both;"></div>
    <p>Start Date</p>
    
     <div class="datetime-from col-12">
        <input type="datetime-local" name="" id="" />
     </div>
    

     <br>

  </div>

  <div style="width:100px; float:right;">
    <p>End Date</p>
     <div class="datetime-from col-12">
       <input type="datetime-local" name="" id="" />
    </div>
  </div>
</div>

    
  </div>
<p style=" font-size:17px;"> Select graph interval</p>

<q-radio val="sec" label="Seconds" v-model="val"/>
<q-radio val="min" label="Minutes" v-model="val"/>
<q-radio val="hr" label="Hours" v-model="val"/>
<q-radio val="day" label="Days" v-model="val"/>

</div>

<div style="clear: both;"></div>
</template>
<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      val: ref(true)
    }
  }
}
</script>

