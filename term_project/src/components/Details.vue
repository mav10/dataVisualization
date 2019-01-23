<template>
  <div>
      <b-tabs v-model="selected">
          <b-tab title="Overview">
              <br>
              <b-row v-if="overview !== null">
                  <b-col cols="12" md="8" style="text-align: left">
                      <p>Date of repar: {{repair.date}}</p>
                      <p>Place: {{repair.place.titile}}</p>
                      <p>Master: {{repair.master.name}}</p>
                      <p>Works categories:</p>
                      <p>{{overview.kindsWork}}</p>
                  </b-col>
                  <b-col cols="6" md="4">
                      <div>
                          <p>Common work's price: {{overview.workSum}}</p>
                          <p>Common compinents's price: {{overview.componentsSum}}</p>
                          <hr>
                          <h4>Common sum: {{overview.commonSum}}</h4>
                      </div>
                  </b-col>
              </b-row>
          </b-tab>
          <b-tab title="Price tables">
              <b-row>
                  <b-col>
                      <b-container v-if="works.length > 0" class="bv-example-row">
                          <b-table striped hover :items="works" :fields="workFields"></b-table>
                      </b-container>
                  </b-col>
                  <b-col>
                      <b-container v-if="components.length > 0" class="bv-example-row">
                          <b-table striped hover :items="components" :fields="componentFields"></b-table>
                      </b-container>
                  </b-col>
              </b-row>
          </b-tab>
          <b-tab title="Works">
              <b-row>
                  <b-col md="2"></b-col>
                  <b-col md="4">
                      <ve-pie :data="workPieData" :settings="workDonutChartSettings"></ve-pie>
                  </b-col>
                  <b-col md="4">
                      <ve-histogram :data="workBarData" ></ve-histogram>
                  </b-col>
                  <b-col md="2"></b-col>
              </b-row>
          </b-tab>
          <b-tab title="Components">
              <h4>Components from shop {{repair.place.titile}}</h4>
              <div style="height: 400px; weight: 300px">
                  <l-map :zoom="zoom" :center="center">
                      <l-tile-layer :url="url"></l-tile-layer>
                      <l-marker v-for="(marker, index) in markers" :key="index" :lat-lng="marker"></l-marker>
                  </l-map>
              </div>
          </b-tab>
      </b-tabs>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import VePie from 'v-charts/lib/pie.common'
import VeHistogram from 'v-charts/lib/histogram.common.js'
import Vue from 'vue';
import { L, LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css'
import Highcharts from 'highcharts/highmaps'
import HighCharts from 'v-highcharts'

// global register
Vue.use(HighCharts);
Vue.use(Highcharts);

Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

export default {
  components: { VePie, VeHistogram,  },
  name: "Details",
  data() {
    return {
        zoom:13,
        center: L.latLng(56.459022, 84.982145),
        url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
        id: 0,
        selected: 1,
        workFields: [
            {
                key: 'titile',
                label: 'Title',
                sortable: false
            },
            {
                key: 'price',
                sortable: true
            },
            {
                key: 'category',
                sortable:false
            }
        ],
        componentFields: [
            {
                key: 'titile',
                label: 'Title',
                sortable: false
            },
            {
                key: 'price',
                sortable: true
            }
        ],
        workDonutChartSettings: {
            dimension: 'date',
            metrics: 'value'
        },
        options: {

            chart: {
                borderWidth: 1
            },

            title: {
                text: 'US population density (/km²)'
            },

            mapNavigation: {
                enabled: true
            },
            series: [{
                data: [
                    {
                        "value": 438,
                        "code": "nj"
                    },
                    {
                        "value": 387.35,
                        "code": "ri"
                    },
                    {
                        "value": 312.68,
                        "code": "ma"
                    },
                    {
                        "value": 271.4,
                        "code": "ct"
                    },
                    {
                        "value": 209.23,
                        "code": "md"
                    },
                    {
                        "value": 195.18,
                        "code": "ny"
                    },
                    {
                        "value": 154.87,
                        "code": "de"
                    },
                    {
                        "value": 114.43,
                        "code": "fl"
                    },
                    {
                        "value": 107.05,
                        "code": "oh"
                    },
                    {
                        "value": 105.8,
                        "code": "pa"
                    },
                    {
                        "value": 86.27,
                        "code": "il"
                    },
                    {
                        "value": 83.85,
                        "code": "ca"
                    },
                    {
                        "value": 72.83,
                        "code": "hi"
                    },
                    {
                        "value": 69.03,
                        "code": "va"
                    },
                    {
                        "value": 67.55,
                        "code": "mi"
                    },
                    {
                        "value": 65.46,
                        "code": "in"
                    },
                    {
                        "value": 63.8,
                        "code": "nc"
                    },
                    {
                        "value": 54.59,
                        "code": "ga"
                    },
                    {
                        "value": 53.29,
                        "code": "tn"
                    },
                    {
                        "value": 53.2,
                        "code": "nh"
                    },
                    {
                        "value": 51.45,
                        "code": "sc"
                    },
                    {
                        "value": 39.61,
                        "code": "la"
                    },
                    {
                        "value": 39.28,
                        "code": "ky"
                    },
                    {
                        "value": 38.13,
                        "code": "wi"
                    },
                    {
                        "value": 34.2,
                        "code": "wa"
                    },
                    {
                        "value": 33.84,
                        "code": "al"
                    },
                    {
                        "value": 31.36,
                        "code": "mo"
                    },
                    {
                        "value": 30.75,
                        "code": "tx"
                    },
                    {
                        "value": 29,
                        "code": "wv"
                    },
                    {
                        "value": 25.41,
                        "code": "vt"
                    },
                    {
                        "value": 23.86,
                        "code": "mn"
                    },
                    {
                        "value": 23.42,
                        "code": "ms"
                    },
                    {
                        "value": 20.22,
                        "code": "ia"
                    },
                    {
                        "value": 19.82,
                        "code": "ar"
                    },
                    {
                        "value": 19.4,
                        "code": "ok"
                    },
                    {
                        "value": 17.43,
                        "code": "az"
                    },
                    {
                        "value": 16.01,
                        "code": "co"
                    },
                    {
                        "value": 15.95,
                        "code": "me"
                    },
                    {
                        "value": 13.76,
                        "code": "or"
                    },
                    {
                        "value": 12.69,
                        "code": "ks"
                    },
                    {
                        "value": 10.5,
                        "code": "ut"
                    },
                    {
                        "value": 8.6,
                        "code": "ne"
                    },
                    {
                        "value": 7.03,
                        "code": "nv"
                    },
                    {
                        "value": 6.04,
                        "code": "id"
                    },
                    {
                        "value": 5.79,
                        "code": "nm"
                    },
                    {
                        "value": 3.84,
                        "code": "sd"
                    },
                    {
                        "value": 3.59,
                        "code": "nd"
                    },
                    {
                        "value": 2.39,
                        "code": "mt"
                    },
                    {
                        "value": 1.96,
                        "code": "wy"
                    },
                    {
                        "value": 0.42,
                        "code": "ak"
                    }
                ],
                mapData: Highcharts.maps['countries/us/us-all'],
                joinBy: ['postal-code', 'code'],
                dataLabels: {
                    enabled: true,
                    color: '#FFFFFF',
                    format: '{point.code}'
                },
                name: 'Population density',
            }]
        }
    };
  },
    watch: {
        selected(value) {
            if (value === 0) {
                const payload = {
                    works: this.works,
                    components: this.components
                }
                this.$store.dispatch('repairs/getOverview', payload)
            }
        }
    },
  computed: mapState({
    works: state => state.repairs.works,
    components: state => state.repairs.components,
      overview: state => state.repairs.overview,
      workPieData: state => state.repairs.workPieData,
      workBarData: state => state.repairs.workBarData,
      repair: state => state.repairs.repair,
      markers: state => state.repairs.markers
  }),
  methods: {
      ...mapActions('repairs', [
        'drawMaps',
      ])
  },
  created() {
      this.id = this.$route.params.id;
      this.$store.dispatch('repairs/getDetails', this.id)
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

</style>
