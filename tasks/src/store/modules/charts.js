import messageService from '../../services/messageService'

const state = {
    organisations: null,
    devices:[],
    statistics: null
}

const getters = {
  devices: state => {
    return state.devices
  }
}

const actions = {
  getDevices ({ commit }) {
    messageService.fetchDevices()
    .then(devices => {
      commit('setDevices', devices)
    })
  },
  showStatistics( {commit}, deviceId) {
    messageService.fetchStat(deviceId)
        .then(stat => {
          commit('setStatistics', stat)
        })
  },
    getOrganisations({commit}) {
      messageService.fetchOrganisation()
          .then(orgs => {
            commit('setOrganisations', orgs)
          })
    },
  getPatientsCount ({ commit }) {
    messageService.fetchPatients()
        .then(patients => {
          commit('setPatients', patients)
        })
  },
}

const mutations = {
  setDevices (state, devices) {
    state.statistics = null
    state.devices = devices
  },
    setOrganisations (state, orgs) {
      state.organisations = orgs;
    },
  clearStat (state) {
    state.statistics = null;
  },
  setStatistics (state, statistics) {
    const lineData = {
      columns: ['date', 'avg'],
      rows: statistics.map(function (stat) {
        return {
          date: stat.therapy_date,
          avg: stat.statistics.avg_index
        }
      })
    }
    const scatterData = {
      columns: ['date', 'therapy', 'transmission', 'th_date'],
      rows: statistics.map(function (stat, index) {
        return {
          date: `1/${index + 1}`,
          therapy: Date.parse(stat.therapy_date)/100000000000,
          transmission: Date.parse(stat.transmission_date)/100000000000,
          th_date: stat.therapy_date,
          tr_date: stat.transmission_date
        }
      })
    }
    state.statistics = {lineData, scatterData}
  },
  setPatients (state, patients) {
    const counters = [];
    patients.forEach(function (patient) {
      if(counters[patient.organisation.pk] != null){
        counters[patient.organisation.pk] = {
          org: patient.organisation.title,
          sum: counters[patient.organisation.pk].sum + 1
        };
      }else{
        counters[patient.organisation.pk] = {
              org: patient.organisation.title,
              sum: 1
            };
      }
    })
    const dirtyRows = counters.map(function (item, index) {
        return {
          organisation: item.org,
          patients: item.sum
        }
    })
    const barData = {
      columns: ['organisation', 'patients'],
      rows: dirtyRows.filter(item => item !== null)
    }
    state.organisations = barData;
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}