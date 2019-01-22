<template>
    <div>
        <br>
        <div v-if="dates.length > 0">
            <select v-model="selectedOption" v-on:change="onChange">
                <option disabled value="">Please select one</option>
                <option v-for="(item, index) in dates"
                        :value="item.pk"
                        :key="index">
                    {{item.value}}
                </option>
            </select>
        </div>
        <p v-if="temps.length === 0">loading ...</p>
        <div v-if="temps.length > 0">
            <vl-map :load-tiles-while-animating="true" :load-tiles-while-interacting="true" data-projection="EPSG:4326">
                <vl-view :zoom.sync="zoom" :center.sync="center" :rotation.sync="rotation"></vl-view>

                <vl-layer-tile id="osm">
                    <vl-source-osm></vl-source-osm>
                </vl-layer-tile>

                <vl-feature v-for="(marker, index) in markers" :properties="marker" :key="index">
                    <div v-if="marker">
                        <vl-geom-point :color="[254, 178, 76, 0.7]" :coordinates="[Number(marker.lng), Number(marker.lat)]">{{marker.temp}}</vl-geom-point>
                    </div>
                </vl-feature>
            </vl-map>
        </div>
        <p v-if="files.length === 0">No imported files</p>
        <table v-if="files.length > 0">
            <thead>
            <tr>
                <th>
                    #
                </th>
                <th>
                    FileName
                </th>
                <th>
                    Description
                </th>
                <th>
                    Action
                </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(file, index) in files" :key="index">
                <td>
                    {{index + 1}}
                </td>
                <td>
                    {{file.value}}
                </td>
                <td>
                    {{file.description}}
                </td>
                <td>
                    <button v-on:click="showDates(file.pk)">Show Dates</button>
                </td>
            </tr>
            </tbody>
        </table>

    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import Vue from 'vue';
    import VueFusionCharts from 'vue-fusioncharts';
    import FusionCharts from 'fusioncharts';
    import Maps from 'fusioncharts/fusioncharts.maps'
    import World from 'fusioncharts/maps/fusioncharts.world'
    import GmapCustomMarker from 'vue2-gmap-custom-marker';
    import VueLayers from 'vuelayers'
    import 'vuelayers/lib/style.css' // needs css-loader

    Vue.use(VueLayers)

    //import the theme
    import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';

    // register VueFusionCharts component
    Vue.use(VueFusionCharts, FusionCharts, Maps, World, FusionTheme)



    export default {
        name: "netcdf",
        components: {
            'gmap-custom-marker': GmapCustomMarker
        },

        data: function () {
            return {
                selectedOption: '',
                loading: true,
                selectedFeatures: [],
                center: [114.160147, 22.35201],
                zoom: 11,
                rotation: 0,
                images: {}
            };
        },
        computed: mapState({
            files: state => state.netcdf.files,
            dates: state => state.netcdf.dates,
            temps: state => state.netcdf.temps,
            markers: state => state.netcdf.markers,
        }),
        methods: {
            isMarkerSelected: function(marker) {
                if (this.selectedFeatures.length === 0) {
                    return false;
                }
                return this.selectedFeatures[0].properties.index === marker.index;
            },
            featureUpdated: function(features) {
                this.$emit('featureSelected', features.length > 0 ? features[0] : null);
                this.selectedFeatures = features;
            },
            onChange() {
                this.$store.dispatch('netcdf/showMap', this.selectedOption)
            },
            ...mapActions('netcdf', [
                'showDates',
                'showMap'
            ]),
        },
        created() {
            this.$store.dispatch('netcdf/getFiles')
        }
    };
</script>

<style scoped>
    .highcharts {
        width: 400px;
        height: 400px;
    }
    hr {
        max-width: 65%;
    }

    #app {
        height: 100%;
        margin: 0;
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
