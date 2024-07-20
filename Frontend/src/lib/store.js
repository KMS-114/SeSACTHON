import { writable } from 'svelte/store';

export const isLoggedIn = writable(false); // 초기 로그인 상태는 false로 설정
export const user = writable(null); // 사용자 정보
export const userType = writable(null); // 사용자 유형 (고용주 또는 지원자)

const persist_storage = (key, initValue) => {
    const storedValueStr = localStorage.getItem(key)
    const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue)
    store.subscribe((val) => {
        localStorage.setItem(key, JSON.stringify(val))
    })
    return store
}

export const page = persist_storage("page", 0)