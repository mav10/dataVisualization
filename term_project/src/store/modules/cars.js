import messageService from '../../services/messageService'
import {adjustBar} from "./repairs";
import {getCategoryValue} from "./utils";
import {L} from "vue2-leaflet";

const state = {
  cars: [],
  repairs: [],
    workBarData:{},
    workLineData: {},
    componentLineData: {}
}

const getters = {
  cars: state => {
    return state.cars
  }
}

const actions = {
  getCars ({ commit }) {
    messageService.fetchCars()
    .then(cars => {
      commit('setCars', cars)
    })
  },
  showRepairs ({commit}, carId) {
    messageService.fetchRepairs(carId)
        .then(repairs => {
          commit('setRepairs', repairs)
        })

    messageService.fetchWorksByCar(carId)
        .then(works => {
            commit('setWorks', works)
        })

    messageService.fetchComponentsByCar(carId)
      .then(components => {
          commit('setComponents', components)
      })

    messageService.fetchPlaces()
        .then(places => {
          commit('setPlaces', places)
        })
  },
}

const mutations = {
  setCars (state, cars) {
    state.repairs = []
    state.cars = cars
  },
  setRepairs (state, repairs) {
    const newRepairs = repairs.map(function (item) {
      return {
        ...item,
        place: item.place.titile + ', ' + item.place.address,
        masterName: item.master.name,
        isСertifiedRepair: item.master.isMaster
      }
    })
    state.repairs = newRepairs
  },
  setWorks (state, works) {
      works.forEach(x => x.category = getCategoryValue(x.category))
      const dates = adjustDates(works)
      dates.forEach(function (date) {
          date.sumWork = works.reduce((a, b) => {
              if(b.repair.date === date.date)
                  return a + b.price;
              else
                  return a;
          }, 0)
      })
      state.workLineData = {
          columns: ['date', 'sumWork', 'sumCom'],
          rows: dates
      }
      state.workBarData = adjustBar(works)
  },
    setComponents (state, components) {
        const dates = adjustDates(components)
        dates.forEach(function (date) {
            date.sumCom = components.reduce((a, b) => {
                if(b.repair.date === date.date)
                    return a + b.price;
                else
                    return a;
            }, 0)
        })
        state.componentLineData = {
            columns: ['date', 'sumCom'],
            rows: dates
        }
        console.log(state.componentLineData)
    },
  setPlaces (state, places) {
    state.markers = places.map(function (x) {
      return L.latLng(x.latitude, x.longitude)
    })
  }
}

function adjustDates(incomming) {
    return getUniqueDates(incomming).map(function (x) {
        return {
            date: x,
            sumCom: 0,
            sumWork: 0
        }
    })
}

function getUniqueDates(worksOrDetails) {
    const dates = worksOrDetails.map(x => x.repair.date)
    return dates.filter(function (work, index, self) {
        return self.indexOf(work) === index;
    })
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}