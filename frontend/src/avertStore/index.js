import { reactive } from "vue"

const state = reactive({
    keystrokes: 0,
    mouseactions: 0,
    windowhistory: 0,
    screenshots: 0,
    videos: 0,
    networkdata: 0,
    systemcalls: 0,
    processes: 0,
});

export default {
  state,
};