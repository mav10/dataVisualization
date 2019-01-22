import api from '@/services/api'

export default function Get(endpoint) {
    return api.get(endpoint)
        .then(response => response.data);
}