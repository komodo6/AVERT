<template>
    <div>
        <div class="row">
            <div class="col">
                <div class="row">
                    <div class="col">
                        <q-list bordered>
                            <q-item>
                                <q-item-section>
                                    <q-item-label>Record Screen</q-item-label>
                                </q-item-section>
                                <q-item-section>
                                    <q-toggle color="primary" v-model="value" />
                                </q-item-section>
                            </q-item>
                            <q-item>
                                <q-item-section>
                                    <q-item-label>Record Keystrokes</q-item-label>
                                </q-item-section>
                                <q-item-section>
                                    <q-toggle color="primary" v-model="value" />
                                </q-item-section>
                            </q-item>
                            <q-item>
                                <q-item-section>
                                    <q-item-label>Record Screenshots</q-item-label>
                                </q-item-section>
                                <q-item-section>
                                    <q-toggle color="primary" v-model="value" />
                                </q-item-section>
                            </q-item>
                            <q-item>
                                <q-item-section>
                                    <q-item-label>Record PCAP</q-item-label>
                                </q-item-section>
                                <q-item-section>
                                    <q-toggle color="primary" v-model="value" />
                                </q-item-section>
                            </q-item>
                            <q-item>
                                <q-item-section>
                                    <q-item-label>Record Window History</q-item-label>
                                </q-item-section>
                                <q-item-section>
                                    <q-toggle color="primary" v-model="value" />
                                </q-item-section>
                            </q-item>
                            <q-item>
                                <q-item-section>
                                    <q-item-label>Record Cursor</q-item-label>
                                </q-item-section>
                                <q-item-section>
                                    <q-toggle color="primary" v-model="value" />
                                </q-item-section>
                            </q-item>
                        </q-list>
                    </div>
                    <div class="col">
                        <q-list bordered>
                            <q-item>
                                <q-item-section>
                                    <q-item-label>PCAP Creation Interval</q-item-label>
                                </q-item-section>
                                <q-item-section>
                                    <q-input color="primary" v-model="text"/>
                                </q-item-section>
                                <q-item-section>
                                    <q-select v-model="model" :options="options" label="Interval" />
                                </q-item-section>
                            </q-item>
                            <q-item>
                                <q-item-section>
                                    <q-item-label>Idle Recording Threshold</q-item-label>
                                </q-item-section>
                                <q-item-section>
                                    <q-input color="primary" v-model="text"/>
                                </q-item-section>
                                <q-item-section>
                                    <q-select v-model="model" :options="options" label="Interval" />
                                </q-item-section>
                            </q-item>
                            <q-item>
                                <q-item-section>
                                    <q-item-label>Process Capture Interval</q-item-label>
                                </q-item-section>
                                <q-item-section>
                                    <q-input color="primary" v-model="text"/>
                                </q-item-section>
                                <q-item-section>
                                    <q-select v-model="model" :options="options" label="Interval" />
                                </q-item-section>
                            </q-item>
                        </q-list>
                    </div>
                </div>
            </div>
            <div class="col">
                .col
            </div>
        </div>
        <div class="row">
            <div class="col">
                .col
            </div>
        </div>
    </div>
</template>
<script>
import { ref } from 'vue'
export default {
    setup(){
        return {
            value: ref(true),
            model: ref(null),
            options: [
            'Minutes', 'Seconds',
            ],
            text: ref('')
        }
    }
}
</script>
<style lang="">
    
</style>