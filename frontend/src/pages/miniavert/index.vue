<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-toolbar-title>
          miniAVERT
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

   

    <q-page-container>
      <br>
      <br>
      <br>
      <div class="column items-center" style="height: 150px">
      <div class="col">
        <q-toggle
        systemcall = href(true)
        v-model= "systemcall"
        checked-icon="check"
        color="blue"
        label="Record System Calls"
        unchecked-icon="clear"
      />
      <br>
      <q-toggle
        process = href(true)
        v-model= "process"
        checked-icon="check"
        color="blue"
        label="Record Processes"
        unchecked-icon="clear"
      />
      <br> 
      <q-toggle
        screen = href(true)
        v-model= "screen"
        checked-icon="check"
        color="blue"
        label="Record Screen"
        unchecked-icon="clear"
      />
      <br>
      <q-toggle
        keystroke = href(true)
        v-model= "keystroke"
        checked-icon="check"
        color="blue"
        label="Record Keystroke"
        unchecked-icon="clear"
      />
      <br>
      <q-toggle
        pcap = href(true)
        v-model= "pcap"
        checked-icon="check"
        color="blue"
        label="Record PCAP Data"
        unchecked-icon="clear"
      />
      <br>
      <q-toggle
        windowhistory = href(true)
        v-model= "windowhistory"
        checked-icon="check"
        color="blue"
        label="Record Window History"
        unchecked-icon="clear"
      />
      <br>
      <q-toggle
        mouseaction = href(true)
        v-model= "mouseaction"
        checked-icon="check"
        color="blue"
        label="Record Mouse Actions"
        unchecked-icon="clear"
      />
      <br>
      <q-toggle
        screenshot = href(true)
        v-model= "screenshot"
        checked-icon="check"
        color="blue"
        label="Record Screenshot"
        unchecked-icon="clear"
      />
      <br>
      <q-toggle
        v-model= "value"
        checked-icon="check"
        color="blue"
        label="Record All Artifact"
        unchecked-icon="clear"
      />
      <br>
      Screen Record
      <q-btn-group push>
        <q-btn push label = "Start" color="grey-9 q-mx-sm" />
        <q-btn push label = "Pause" color="grey-9 q-mx-sm" />
        <q-btn push label = "Stop" color="grey-9 q-mx-sm" />
      </q-btn-group>
      <br>
      <br>
      <br>
      Capture Screenshot        <q-btn push text-align center label = "Take Screenshot" color="grey-9 q-mx-sm" />
      

      </div>
      </div>




    </q-page-container>

  </q-layout>
</template>
