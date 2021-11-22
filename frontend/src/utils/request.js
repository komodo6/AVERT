import {api} from 'src/boot/axios'
import avertStore from "src/avertStore"

export const fetchKeystrokes = async () => {
    await api.get('/keystrokes').then((response) => {
        avertStore.state.keystrokes = response.data 
    })
}


export const fetchMouseActions = async () => {
    await api.get('/mouseactions').then((response) => {
        avertStore.state.mouseactions = response.data 
    })
}




// export default fetchKeystrokes, 
