import messageService from '../../services/messageService'

const state = {
    dates: [],
    temps:[],
    files: []
}

const getters = {
  files: state => {
    return state.files
  }
}

const actions = {
  getFiles ({ commit }) {
    messageService.fetchMapFiles()
    .then(files => {
      commit('setFiles', files)
    })
  },
  showDates( {commit}, fileId) {
    messageService.fetchMapDates(fileId)
        .then(dates => {
          commit('setDates', dates)
        })
  },
  showMap( {commit}, dateId) {
    messageService.fetchMapTemperature(dateId)
        .then(temps => {
          commit('setTemps', temps)
        })
  }
}

const mutations = {
  setFiles (state, files) {
    state.dates = []
    state.temps = []
    state.files = files
  },
  setDates (state, dates) {
    state.dates = dates;
  },
  setTemps (state, temps) {
    state.temps = temps
      state.markers = temps.map(function (marker) {
          return {
              lat: marker.latitude.value,
              lng: marker.longitude.value,
              tmp: marker.value
          }
      }) 
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}