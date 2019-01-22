<template>
    <div class="hello">
        <img src='@/assets/logo-vue.png' style="width: 250px"/>

        <hr/>
        <h3>Patients on Database</h3>
        <table v-if="stats !== null && patients.length > 0">
            <thead>
            <tr>
                <th>
                    number
                </th>
                <th>
                    Index A
                </th>
                <th>
                    Index B
                </th>
                <th>
                    Index C
                </th>
                <th>
                    Total Index
                </th>
                <th>
                    Therapy date
                </th>
                <th>
                    Transmission date
                </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(stat, index) in stats" :key="index">
                <td>
                    {{index}}
                </td>
                <td>
                    {{stat.statistics.index_A}}
                </td>
                <td>
                    {{stat.statistics.index_B}}
                </td>
                <td>
                    {{stat.statistics.index_C}}
                </td>
                <td>
                    {{stat.statistics.avg_index}}
                </td>
                <td>
                    {{stat.therapy_date}}
                </td>
                <td>
                    {{stat.transmission_date}}
                </td>
            </tr>
            </tbody>
        </table>

        <table v-if="device !== null && patients.length > 0">
            <thead>
            <tr>
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
            <tr>
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
        <p v-if="patients.length === 0">No Patients</p>
        <table v-if="patients.length > 0">
            <thead>
            <tr>
                <th>
                    Number
                </th>
                <th>
                    Name
                </th>
                <th>
                    Gender
                </th>
                <th>
                    Birthday date
                </th>
                <th>
                    Last Visit date
                </th>
                <th>
                    Action
                </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(patient, index) in patients" :key="index">
                <td>
                    {{index + 1}}
                </td>
                <td>
                    {{patient.name}}
                </td>
                <td>
                    {{patient.gender}}
                </td>
                <td>
                    {{patient.birthday_date}}
                </td>
                <td>
                    {{patient.lastVisit_date}}
                </td>
                <td>
                    <button v-on:click="showDevice(patient.pk)">Show Device</button>
                </td>
            </tr>
            </tbody>
        </table>

        <p v-if="organisations.length === 0">No Organisations</p>
        <table v-if="organisations.length > 0">
            <thead>
            <tr>
                <th>
                    Number
                </th>
                <th>
                    Title
                </th>
                <th>
                    Address
                </th>
                <th>
                    Contacts
                </th>
                <th>
                    Action
                </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(org, index) in organisations" :key="index">
                <td>
                    {{index + 1}}
                </td>
                <td>
                    {{org.title}}
                </td>
                <td>
                    {{org.address}}
                </td>
                <td>
                    {{org.contacts}}
                </td>
                <td>
                    <button v-on:click="showPatients(org.pk)">Show Patients</button>
                </td>
            </tr>
            </tbody>
        </table>

    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'

    export default {
        name: "Patients",
        data() {
            return {
                name: "",
                gender: "",
            };
        },
        computed: mapState({
            organisations: state => state.patients.organisations,
            patients: state => state.patients.patients,
            device: state => state.patients.currentDevice,
            stats: state => state.patients.statistics
        }),
        methods: mapActions('patients', [
            'showDevice',
            'showStatistics',
            'showPatients'
        ]),
        created() {
            this.$store.dispatch('patients/getOrganisations')
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
