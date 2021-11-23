import {api} from 'src/boot/axios'
import avertStore from "src/avertStore"
//import { apply } from 'core-js/fn/reflect';

export const fetchKeystrokes = async () => {
    await api.get('/keystrokes/count').then((response) => {
        console.log(response.data);
        avertStore.state.keystrokes = response.data
    })
}

export const fetchMouseActions = async () => {
    await api.get('/mouseactions/count').then((response) => {
        console.log(response.data)
        avertStore.state.mouseactions = response.data 
    })
}

export const fetchScreenshots = async () => {
    await api.get('/screenshots/count').then((response) => {
        console.log(response.data)
        avertStore.state.screenshots = response.data 
    })
}

export const fetchProcesses = async () => {
    await api.get('/processes/count').then((response) => {
        console.log(response.data)
        avertStore.state.processes = response.data 
    })
}

export const fetchWindowHistory = async () => {
    await api.get('/windows/count').then((response) => {
        console.log(response.data)
        avertStore.state.windowhistory = response.data 
    })
}

export const fetchSystemCalls = async () => {
    await api.get('/systemcalls/count').then((response) => {
        console.log(response.data)
        avertStore.state.systemcalls = response.data 
    })
}

export const fetchVideos = async () => {
    await api.get('/videos/count').then((response) => {
        console.log(response.data)
        avertStore.state.videos = response.data 
    })
}
    





// export default fetchKeystrokes, 
