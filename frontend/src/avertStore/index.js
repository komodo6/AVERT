import { reactive } from "vue"

const state = reactive({
    keystrokesCount: 0,
    mouseactionsCount: 0,
    windowhistoryCount: 0,
    screenshotsCount: 0,
    videosCount: 0,
    networkdataCount: 0,
    systemcallsCount: 0,
    processesCount: 0,
    keystrokes: [],
    mouseactions: [],
    windowhistory: [],
    screenshots: [],
    videos: [],
    networkdata: [],
    systemcalls: [],
    processes: [],
});

export default {
  state,
};