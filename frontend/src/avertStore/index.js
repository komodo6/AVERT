import { reactive } from "vue"

const state = reactive({
    keystrokes: [],
    mouseactions: [],
    windowhistory: [],
    screenshots: [],
    videos: [],
    networkdata: [],
    systemcalls: [],
    processes: [],
    //TODO ADD REST
})

export default {
    state
}