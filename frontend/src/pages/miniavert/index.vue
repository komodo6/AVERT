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
        systemcall = href(false)
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
        label="Record System Calls"
        unchecked-icon="clear"
      />
      <br> 
      <q-toggle
        process = href(true)
        v-model= "process"
        checked-icon="check"
        color="blue"
        label="Record System Calls"
        unchecked-icon="clear"
      />
      <br>
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
