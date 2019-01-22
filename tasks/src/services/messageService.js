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
  fetchPatients() {
    return Get(`patients/`);
  },
  fetchStat(deviceId) {
    return Get(`therapy?device=${deviceId}`);
  },
  fetchOrganisation() {
        return Get(`organisations/`);
  },
    fetchPatientsByOrganisation(orgId) {
        return Get(`patients?organisation=${orgId}`);
    },
    fetchDevices() {
      return Get(`devices/`);
    },
  fetchMapFiles() {
    return Get(`files/`)
  },
  fetchMapDates(fileId) {
    return Get(`dates?file=${fileId}`)
  }
  ,
  fetchMapTemperature(dateId) {
    return Get(`temperature/?date=${dateId}`)
  }

}