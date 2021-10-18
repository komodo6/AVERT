<template>
  <div style="width:1000px;">

  <div style="width:500px; float:left;">
  <div class="q-pa-md">
    <div class="q-gutter-sm">
      <h1 style="font-size:30px;padding-left:5px;">Visualization</h1>
      <p style="padding-left:20px; font-size:17px;"> Select type of graph</p>
      <q-radio  val="tl" label="Timeline" />
      <q-radio  val="bg" label="Bar Graph" />
      <q-radio  val="pc" label="Pie Chart" />
      <q-radio  val="cpu" label="CPU Usage" />
      <br>
      <br>
      
    </div>
  </div>
   <div class="q-pa-md">
    <div class="q-gutter-sm">
      <p style="padding-left:20px; font-size:17px;"> Select data to include</p>
      <q-checkbox style="padding-right:60px;" label="Select All"  />
      <q-checkbox  label="Screenshots" /><br>
      <q-checkbox  label="Mouse Movements" />
      <q-checkbox  label="Window Histories" /><br>
      <q-checkbox style="padding-right:84px;" label="PCAP" />
      <q-checkbox  label="Keystrokes" /><br>
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
    
     <!--
     <div class="q-pa-md" style="max-width: 300px">
    <q-input filled v-model="date" mask="date" :rules="['date']">
      <template v-slot:append>
        <q-icon name="event" class="cursor-pointer">
          <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
            <q-date v-model="date">
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-date>
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>
  </div>
  -->
     <br>
  <!--   
     <p>Start Time</p>
  <div class="q-pa-md">
    <div class="q-gutter-sm row">
      <q-input filled v-model="timeWithSeconds" mask="fulltime" :rules="['fulltime']">
        <template v-slot:append>
          <q-icon name="access_time" class="cursor-pointer">
            <q-popup-proxy transition-show="scale" transition-hide="scale">
              <q-time
                v-model="timeWithSeconds"
                with-seconds
                format24h
              >
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-time>
            </q-popup-proxy>
          </q-icon>
        </template>
      </q-input>
    </div>
   </div>
   -->
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
<!--
 <input type="radio" id="html" name="fav_language" value="HTML">
  <label for="html">HTML</label><br>
 <input type="radio" id="html" name="fav_language" value="HTML">
  <label for="html">HTML</label><br>
-->
<q-radio val="sec" label="Seconds" />
<q-radio val="min" label="Minutes" />
<q-radio val="hr" label="Hours" />
<q-radio val="day" label="Days" />

</div>
<div style="clear: both;"></div>
</template>


<!--
<template>
  <div>
    <body>
    <h1 style="font-size:30px;padding-left:5px;">Visualization</h1>
    <p style="padding-left:20px; font-size:17px;"> Select type of graph</p>
    
     <q-radio v-model="shape" val="line" label="Timeline" />
     <q-radio v-model="shape" val="line" label="Bar graph" />
     <q-radio v-model="shape" val="line" label="Pie Chart" />
     <q-radio v-model="shape" val="line" label="CPU Usage" />
       
    <input type="checkbox" id = "tl" name = "tl" >
    <label for="tl" style="padding-right:10px;"> Timeline </label>
    <input type="checkbox" id = "bg" name = "bg">
    <label for="bg" style="padding-right:20px;"> Bar Graph </label>
    <input type="checkbox" id = "pc" name = "pc">
    <label for="pc" style="padding-right:20px;"> Pie Chart </label>
    <input type="checkbox" id = "cpu" name = "cpu">
    <label for="cpu" style="padding-right:20px;"> CPU Usage </label>
   
<br>
    <p style="padding-left:20px; font-size:17px;"> Select data to include</p>
    </body>
  </div>
 -->
