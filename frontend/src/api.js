import axios from 'axios'

var instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  URL: process.env.VUE_APP_BASE_URL
})

export default {
  /**
   * Get API
   * @param {string} path API path
   * @param {Object} options Get options
   */
  get (path, options) {
    return instance.get(path, options)
  },

  /**
   * Patch API
   * @param {string} path API path
   * @param {Object} data Patch data
   * @param {Object} options Patch options
   */
  patch (path, data, options) {
    return instance.patch(path, data, options)
  },

  /**
   * Post API
   * @param {string} path API path
   * @param {Object} data Post data
   * @param {Object} options Post options
   */
  post (path, data, options) {
    return instance.post(path, data, options)
  },
  /**
   * Delete API
   * @param {string} path API path
   * @param {Object} options Delete options
   */
  delete (path, options) {
    return instance.delete(path, options)
  },
  instance

}
