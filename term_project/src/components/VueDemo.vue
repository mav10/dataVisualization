<template>
  <div class="hello">
    <img src='@/assets/Car.png'>
      <b-container v-if="repairs.length > 0" class="bv-example-row">
        <b-row>
            <h3>Work summary</h3>
            <ve-line :data="componentLineData" ></ve-line>
        </b-row>
        <b-row>
          <b-col>
              <b-table striped hover :items="repairs" :fields="repairFields"  @row-clicked="details" ></b-table>
          </b-col>
          <b-col md="6">
            <h3>Sum by category</h3>
            <ve-pie :data="workBarData" :settings="workDonutChartSettings"></ve-pie>
            <h3>Count by category</h3>
            <ve-pie :data="workBarData" :settings="workChartSettings"></ve-pie>
          </b-col>
        </b-row>
        <div style="height: 400px; weight: 300px">
          <l-map :zoom="zoom" :center="center">
            <l-tile-layer :url="url"></l-tile-layer>
            <l-marker v-for="(marker, index) in markers" :key="index" :lat-lng="marker"></l-marker>
          </l-map>
        </div>
      </b-container>
    <p v-if="cars.length === 0">No cars in book</p>
    <b-container v-if="cars.length > 0" class="bv-example-row">
      <b-row>
        <b-col v-for="(car, index) in cars" :key="index">
          <b-card  overlay
                   img-src="http://pngimages.net/sites/default/files/car-png-image-44997.png"
                   img-alt="Image"
                   img-top
                   style="max-width: 20rem;"
                   class="mb-2">
            <h4>{{ car.name }}</h4>
            <p class="card-text">
              Car millage: {{car.milage}} km
            </p>
            <b-button @click="showRepairs(car.pk)" style="position: relative; top: 80px;">
              Show repairs history
            </b-button>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import Vue from 'vue'
  import { mapState, mapActions } from 'vuex'
  import BootstrapVue from 'bootstrap-vue'
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'
  import VePie from 'v-charts/lib/pie.common'
  import VeLine from 'v-charts/lib/line.common'
  import { L, LMap, LTileLayer, LMarker } from 'vue2-leaflet';
  import 'leaflet/dist/leaflet.css'
  Vue.component('l-map', LMap);
  Vue.component('l-tile-layer', LTileLayer);
  Vue.component('l-marker', LMarker);

  delete L.Icon.Default.prototype._getIconUrl;

  L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
  });



  Vue.use(BootstrapVue);

  export default {
    components: { VePie, VeLine},
    name: "main",
    data () {
      return {
        zoom:10,
        center: L.latLng(56.459022, 84.982145),
        url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
        slide: 0,
        sliding: null,
        repairFields: [
          {
            key: 'place',
            sortable: false
          },
          {
            key: 'milage',
            sortable: true
          },
          {
            key: 'date',
            sortable: true,
          },
          {
            key: 'masterName',
            sortable: false,
          },
          {
            key: 'isСertifiedRepair',
            sortable: false,
            label: 'Сertified Repair'
          }
        ],
        workDonutChartSettings: {
          dimension: 'date',
          metrics: 'sum'
        },
        workChartSettings: {
          dimension: 'date',
          metrics: 'value'
        }
      }
    },
    computed: mapState({
      cars: state => state.cars.cars,
      repairs: state => state.cars.repairs,
      workBarData: state => state.cars.workBarData,
      markers: state => state.cars.markers,
      componentLineData: state => state.cars.componentLineData,
      workLineData: state => state.cars.workLineData
    }),
    methods: {
      details(item) {
        this.$router.push(`/repair/${item.pk}`)
      },
      ...mapActions('cars', [
        'showRepairs'
      ])
    },
    created() {
      this.$store.dispatch('cars/getCars')
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card {
    border: none
  }
  .card-img-top{
    margin-left: 10px;
  }
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

img {
  width: 250px;
}

</style>
