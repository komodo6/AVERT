<template>
  <div id="chart">
    <apexchart
      type="line"
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
  fetchMouseActionsTimeline,
  fetchScreenshots,
  fetchProcesses,
  fetchWindowHistory,
  fetchSystemCalls,
  fetchVideos,
} from "src/utils/request.js";
import axios from 'axios'; 
// import {chartOptions} from "./timelineoption.js";

export default {
  name: "TimeLine",
  props:['startTime','endTime','selectedArtifacts'],
  components: {
    apexchart: VueApexCharts,
  },
  async created(){
    var selectedArtifacts = []
    
    var startTime = "";
    var endTime = "";
    startTime = this.$props.startTime.replace('T',' ')
    endTime = this.$props.endTime.replace('T',' ')
    console.log('startTime: ' + startTime )
    console.log('endTime: ' + endTime )


    

    const maTimeline = await axios.post("http://localhost:5000/mouseactions/timeline", {
      start: startTime,
      end: endTime,
    })

    const ksTimeline = await axios.post("http://localhost:5000/keystrokes/timeline", {
      start: startTime,
      end: endTime,
    })

    const psTimeline = await axios.post("http://localhost:5000/processes/timeline", {
      start: startTime,
      end: endTime,
    })

    const whTimeline = await axios.post("http://localhost:5000/windows/timeline", {
      start: startTime,
      end: endTime,
    })

    const scTimeline = await axios.post("http://localhost:5000/screenshots/timeline", {
      start: startTime,
      end: endTime,
    })

    const vTimeline = await axios.post("http://localhost:5000/videos/timeline", {
      start: startTime,
      end: endTime,
    })


    this.$props.selectedArtifacts.forEach(item =>{
      if(item === "mouseActions"){
        selectedArtifacts.push({
          name: "Mouse Action",
          data: maTimeline['data']['r_intervals'],
        })
      }
      if(item === "keyStrokes"){
        selectedArtifacts.push(
        {
          name: "Keystrokes",
          data: ksTimeline['data']['r_intervals']
        }
        )
      }
      if(item === "processes"){
        selectedArtifacts.push(
        {
          name: "Process",
          data: psTimeline['data']['r_intervals']
        }
        )
      }
      if(item === "windowHistory"){
        selectedArtifacts.push(
        {
          name: "Window History",
          data: whTimeline['data']['r_intervals']
        }
        )
      }
      if (item === "networkData" ){
        selectedArtifacts.push(
        {
          name: "Network",
          data: [0]
        }
        )
      }
      if (item === "screenShots" ){
        selectedArtifacts.push(
        {
          name: "Screen Shots",
          data: vTimeline['data']['r_intervals']
        }
        )
      }
      if (item === "videos" ){
        selectedArtifacts.push(
        {
          name: "Videos",
          data: vTimeline['data']['r_intervals']
        }
        )
      }

        


    });

  
    console.log('maTimeline' + JSON.stringify(maTimeline) )
    console.log(maTimeline['data']['r_intervals'])

    // this.series= [
    //     {
    //       name: "Mouse Action",
    //       data: maTimeline['data']['r_intervals'],
    //     },
    //     {
    //       name: "Keystrokes",
    //       data: ksTimeline['data']['r_intervals']
    //     },
    //     {
    //       name: "Process",
    //       data: psTimeline['data']['r_intervals']
    //     },
    //     {
    //       name: "Window History",
    //       data: whTimeline['data']['r_intervals']
    //     },
    //     {
    //       name: "Network",
    //       data: [0]
    //     }
    //     ,
    //     {
    //       name: "Screen Shots",
    //       data: scTimeline['data']['r_intervals']
    //     }
    //     ,
    //     {
    //       name: "Videos",
    //       data: vTimeline['data']['r_intervals']
    //     }
    //   ];


   this.series = selectedArtifacts;

    this.chartOptions = {
        chart: {
          // background: '#fff',
          fill: '#000',
          foreColor: '#fff',
          height: 350,
          type: "line",
          zoom: {
            enabled: true,
          },
          animations: {
            background:'#fff',
            enabled: false,
          
          },
        },
        stroke: {
          width: [5, 5, 4],
          curve: "straight",
        },
        tooltip:{
          enabled:true,
          style: {color: '#00ff00'},
          autoTextColor:false,
          label:{
            fill: 'red'
          }
        },
        title: {
          text: "Timeline",
        },
        xaxis: {
            categories:maTimeline['data']['r_times']
        },
      }; 
  },
  data(){
    return{
        series: [
        {
          name: "Mouse Action",
          data:[],
        }
      ],
      chartOptions : {
        chart: {
          height: 350,
          type: "line",
          zoom: {
            enabled: false,
          },
          animations: {
            enabled: true,
          },
        },
        stroke: {
          width: [5, 5, 4],
          curve: "straight",
        },
        title: {
          text: "Timeline",
        },
        xaxis: {
            categories:[]
        },
      } 
    }
  }
  // setup() {
  //   let series = ref([]);
  //   series.value = [
  //       {
  //         name: "Mouse Action",
  //         data:[],
  //       }
  //     ];



  //   let chartOptions = ref({});

  //   chartOptions.value = {
  //       chart: {
  //         height: 350,
  //         type: "line",
  //         zoom: {
  //           enabled: false,
  //         },
  //         animations: {
  //           enabled: true,
  //         },
  //       },
  //       stroke: {
  //         width: [5, 5, 4],
  //         curve: "straight",
  //       },
  //       labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
  //       title: {
  //         text: "Missing data (null values)",
  //       },
  //       xaxis: {
  //           categories:[]
  //       },
  //     };



    
  //   onMounted(() => {
  //     console.log(avertStore.state.mouseActionsTimeline);
  //     fetchMouseActionsTimeline();
  //     chartOptions.value = {
  //       chart: {
  //         height: 350,
  //         type: "line",
  //         zoom: {
  //           enabled: false,
  //         },
  //         animations: {
  //           enabled: true,
  //         },
  //       },
  //       stroke: {
  //         width: [5, 5, 4],
  //         curve: "straight",
  //       },
  //       title: {
  //         text: "Missing data (null values)",
  //       },
  //       xaxis: {
  //           categories:avertStore.state.mouseActionsTimeline['r_times']
  //       },
  //     };

  //     series.value = [
  //       {
  //         name: "Mouse Action",
  //         data:avertStore.state.mouseActionsTimeline['r_intervals'],
  //       }
  //     ];
  //   });
  //   return {
  //     chartOptions,
  //     series,
  //   };
  // },
};
</script>
