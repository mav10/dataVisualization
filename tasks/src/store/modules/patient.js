import messageService from '../../services/messageService'

const state = {
    organisations: [],
  patients: [],
  currentDevice: null,
  statistics: null
}

const getters = {
  patient: state => {
    return state.patients
  }
}

const actions = {
  getPatients ({ commit }) {
    messageService.fetchPatients()
    .then(patients => {
      commit('setPatients', patients)
    })
  },
  showDevice( { commit }, patientId) {
    commit('showDevice', patientId)
    commit('clearStat')
  },
  clearDevice( { commit }) {
    commit('clearDevice')
    commit('clearStat')
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
    showPatients({commit}, orgId) {
        commit('clearPatients')
        commit('clearDevice')
        commit('clearStat')
        messageService.fetchPatientsByOrganisation(orgId)
            .then(patients => {
                commit('setPatients', patients)
            })
    }
}

const mutations = {
  setPatients (state, patients) {
    state.patients = patients
  },
    setOrganisations (state, orgs) {
      state.organisations = orgs;
    },
  showDevice (state, patientId) {
    const patient =  state.patients.find(obj => obj.pk == patientId);
    state.currentDevice = patient.device;
  },
  clearDevice (state) {
    state.currentDevice = null;
  },
  clearStat (state) {
    state.statistics = null;
  },
  setStatistics (state, statistics) {
    state.statistics = statistics
  },
    clearPatients (state) {
      state.patients = null;
    }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}