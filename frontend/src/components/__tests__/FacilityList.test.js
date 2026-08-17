import { flushPromises, mount, RouterLinkStub } from '@vue/test-utils'
import { describe, expect, it, vi } from 'vitest'
import FacilityList from '../FacilityList.vue'

describe('FacilityList', () => {
  it('fetches and renders facilities on mount', async () => {
    const fetchData = vi.fn().mockResolvedValue({
      data: {
        count: 1,
        results: [
          {
            id: 7,
            name: 'Blue Haven',
            address: '1 Main St',
            city: 'Austin',
            state: 'TX',
            zip_code: '78701',
          },
        ],
      },
    })

    const wrapper = mount(FacilityList, {
      props: {
        title: 'Assisted Living Facilities',
        subtitle: 'Directory view',
        kicker: 'Care Directory',
        fetchData,
        detailPath: 'assistedliving',
      },
      global: {
        stubs: {
          RouterLink: RouterLinkStub,
        },
      },
    })

    await flushPromises()

    expect(fetchData).toHaveBeenCalledWith({ page: 1, search: '' })
    expect(wrapper.text()).toContain('Blue Haven')
    expect(wrapper.text()).toContain('1 facilities')
    expect(wrapper.findComponent(RouterLinkStub).props('to')).toBe('/assistedliving/7')
  })

  it('shows an empty state when no facilities are returned', async () => {
    const fetchData = vi.fn().mockResolvedValue({
      data: {
        count: 0,
        results: [],
      },
    })

    const wrapper = mount(FacilityList, {
      props: {
        title: 'Assisted Living Facilities',
        subtitle: 'Directory view',
        kicker: 'Care Directory',
        fetchData,
        detailPath: 'assistedliving',
      },
      global: {
        stubs: {
          RouterLink: RouterLinkStub,
        },
      },
    })

    await flushPromises()

    expect(wrapper.text()).toContain('No assisted living facilities match your search')
  })
})