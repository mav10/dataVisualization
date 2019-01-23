import api from '@/services/api'
import Get from '@/services/apiwrapper';

export default {
  fetchMessages() {
    return Get(`messages/`);
  },
  postMessage(payload) {
    return api.post(`messages/`, payload)
        .then(response => response.data)
  },
  deleteMessage(msgId) {
    return api.delete(`messages/${msgId}`)
        .then(response => response.data)
  },
  fetchPlaces() {
    return Get(`stantions/`);
  },
  fetchCars() {
    return Get(`cars/`);
  },
  fetchRepairs(carId) {
    return Get(`repairs?car=${carId}`)
  },
  fetchRepairById(repairId) {
    return Get(`repairs?id=${repairId}`)
  },
  fetchWorks(repairId) {
    return Get(`works?repair=${repairId}`)
  },
  fetchComponents(repairId) {
    return Get(`components?repair=${repairId}`)
  },
  fetchWorksByCar(carId) {
      return Get(`works?car=${carId}`)
  },
  fetchComponentsByCar(carId) {
    return Get(`components?car=${carId}`)
  }

}