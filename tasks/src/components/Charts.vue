<template>
    <div>
        <div v-if="stats !== null">
            <ve-line :data="stats.lineData"></ve-line>
            <ve-scatter :data="stats.scatterData"  :settings="chartSettings"></ve-scatter>
        </div>
        <p v-if="devices.length === 0">No Devices</p>
        <table v-if="devices.length > 0">
            <thead>
            <tr>
                <th>
                    Number
                </th>
                <th>
                    Title
                </th>
                <th>
                    Model
                </th>
                <th>
                    Serial number
                </th>
                <th>
                    Country of location
                </th>
                <th>
                    Action
                </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(device, index) in devices" :key="index">
                <td>
                    {{index + 1}}
                </td>
                <td>
                    {{device.title}}
                </td>
                <td>
                    {{device.model}}
                </td>
                <td>
                    {{device.serialNuber}}
                </td>
                <td>
                    {{device.country}}
                </td>
                <td>
                    <button v-on:click="showStatistics(device.pk)">Show Statistics</button>
                </td>
            </tr>
            </tbody>
        </table>
        <div v-if="organisations !== null">
            <ve-histogram :data="organisations"></ve-histogram>
        </div>
    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import VeLine from 'v-charts/lib/line.common'
    import VeScatter from 'v-charts/lib/scatter.common'
    import VeHistogram from 'v-charts/lib/histogram.common.js'

    export default {
        components: { VeLine, VeScatter,VeHistogram },
        data () {
            return {
                chartSettings: {
                    min: 15,
                    max: 16
                }
            }
        },
        name: "Charts",
        computed: mapState({
            organisations: state => state.charts.organisations,
            devices: state => state.charts.devices,
            stats: state => state.charts.statistics
        }),
        methods: mapActions('charts', [
            'showStatistics'
        ]),
        created() {
            this.$store.dispatch('charts/getDevices')
            this.$store.dispatch('charts/getPatientsCount')
        }
    };
</script>

<style scoped>
    hr {
        max-width: 65%;
    }

    .msg {
        margin: 0 auto;
        max-width: 30%;
        text-align: left;
        border-bottom: 1px solid #ccc;
        padding: 1rem;
    }

    .msg-index {
        color: #ccc;
        font-size: 0.8rem;
        /* margin-bottom: 0; */
    }

    img {
        width: 250px;
        padding-top: 50px;
        padding-bottom: 50px;
    }

    body {
        font-family: Helvetica Neue, Arial, sans-serif;
        font-size: 14px;
        color: #444;
    }

    table {
        border: 2px solid #42b983;
        border-radius: 3px;
        background-color: #fff;
        margin: 50px;
    }

    th {
        background-color: #42b983;
        color: rgba(255, 255, 255, 0.66);
        cursor: pointer;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }

    td {
        background-color: #f9f9f9;
    }

    th, td {
        min-width: 120px;
        padding: 10px 20px;
    }

    th.active {
        color: #fff;
    }

    th.active .arrow {
        opacity: 1;
    }

    .arrow {
        display: inline-block;
        vertical-align: middle;
        width: 0;
        height: 0;
        margin-left: 5px;
        opacity: 0.66;
    }

    .arrow.asc {
        border-left: 4px solid transparent;
        border-right: 4px solid transparent;
        border-bottom: 4px solid #fff;
    }

    .arrow.dsc {
        border-left: 4px solid transparent;
        border-right: 4px solid transparent;
        border-top: 4px solid #fff;
    }

</style>
