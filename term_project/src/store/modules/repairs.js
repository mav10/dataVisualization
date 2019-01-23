import messageService from '../../services/messageService'
import {getCategoryValue} from "./utils";
import { L } from 'vue2-leaflet';

const state = {
  works:[],
  components:[],
  overview: null,
  workPieData: {},
  workBarData: {},
  repair: null,
  markers: []
}

const getters = {
  details: state => {
    return state.works
  }
}

const actions = {
  getDetails ({ commit }, repairId) {
    commit('cleanState')

    messageService.fetchWorks(repairId)
    .then(works => {
      commit('setWorks', works)
    })

    messageService.fetchRepairById(repairId)
        .then(repair => {
          commit('setRepair', repair)
        })

    messageService.fetchComponents(repairId)
        .then(components => {
          commit('setComponents', components)
        })
  },
  getOverview({commit},payload) {
    commit('calcOverview', payload)
  }
}

const mutations = {
  cleanState (state) {
    state.works = []
    state.components = []
  },
  setWorks (state, works) {
    works.forEach(x => x.category = getCategoryValue(x.category))

    state.works = works
    state.workPieData = adjustPie(works)
    state.workBarData = adjustBar(works)
  },
  setComponents (state, components) {
    state.markers = components.map(function (x) {
        return L.latLng(x.purchase_place.latitude, x.purchase_place.longitude)
    })
    state.components = components
  },
  calcOverview (state, payload) {
    const {works, components} = payload
    const work = works.reduce((a, b) => a + b.price, 0);
    const component = components.reduce((a, b) => a + b.price, 0);

    state.overview = {
      workSum: work,
      componentsSum: component,
      commonSum: work + component,
      kindsWork: getUniqueWorks(works)
    }
  },
  setRepair (state, repair) {
    state.repair = repair[0]
  }
}

function getUniqueWorks(works) {
  const categoryWorks = works.map(x => x.category)
  return categoryWorks.filter(function (work, index, self) {
    return self.indexOf(work) === index;
  })
}

function adjustPie(works) {
  return {
    columns: ['date', 'value'],
    rows: adjustCategories(works)
  }
}

export function adjustBar(works) {
  const categoryWorks = adjustCategories(works)
  categoryWorks.forEach(function (category) {
    category.sum = works.reduce((a, b) => {
      if(b.category === category.date)
        return a + b.price;
      else
        return a;
    }, 0)
  })
  return {
    columns: ['date', 'value', 'sum'],
    rows: categoryWorks
  }
}

function adjustCategories(works) {
  const categoryWorks = getUniqueWorks(works).map(function (x) {
    return {
      date: x,
      value: 0,
      sum: 0
    }
  })
  categoryWorks.forEach(function (category) {
    category.value = works.reduce((a, b) => {
      if(b.category === category.date)
        return a + 1;
      else
        return a;
    }, 0)
  })

  return categoryWorks;
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}