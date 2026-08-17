import { computed, reactive } from 'vue'

const STORAGE_KEY = 'abr-admin-session'

export const authState = reactive({
  token: '',
  username: '',
  expiresAt: '',
})

export const isAuthenticated = computed(() => {
  if (!authState.token || !authState.expiresAt) {
    return false
  }

  return new Date(authState.expiresAt).getTime() > Date.now()
})

export const setAuthSession = (session) => {
  authState.token = session.token
  authState.username = session.username
  authState.expiresAt = session.expires_at || session.expiresAt

  localStorage.setItem(STORAGE_KEY, JSON.stringify({
    token: authState.token,
    username: authState.username,
    expiresAt: authState.expiresAt,
  }))
}

export const clearAuthSession = () => {
  authState.token = ''
  authState.username = ''
  authState.expiresAt = ''
  localStorage.removeItem(STORAGE_KEY)
}

export const initializeAuthSession = () => {
  const savedSession = localStorage.getItem(STORAGE_KEY)
  if (!savedSession) {
    return
  }

  try {
    const parsedSession = JSON.parse(savedSession)
    authState.token = parsedSession.token || ''
    authState.username = parsedSession.username || ''
    authState.expiresAt = parsedSession.expiresAt || ''

    if (!isAuthenticated.value) {
      clearAuthSession()
    }
  } catch {
    clearAuthSession()
  }
}