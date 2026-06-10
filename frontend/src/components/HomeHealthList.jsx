import React from 'react';
import FacilityList from './FacilityList';
import { getHomeHealth } from '../api';

const HomeHealthList = () => {
  return (
    <FacilityList 
      title="Home Health Providers" 
      kicker="Care Directory"
      subtitle="Review home care providers in a more legible table and detail experience."
      fetchData={getHomeHealth}
      detailPath="homehealth"
    />
  );
};

export default HomeHealthList;
