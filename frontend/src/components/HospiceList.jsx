import React from 'react';
import FacilityList from './FacilityList';
import { getHospice } from '../api';

const HospiceList = () => {
  return (
    <FacilityList 
      title="Hospice Care Options" 
      kicker="Care Directory"
      subtitle="Access hospice information with a calmer presentation and consistent actions."
      fetchData={getHospice}
      detailPath="hospice"
    />
  );
};

export default HospiceList;
