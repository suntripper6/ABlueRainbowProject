import React from 'react';
import FacilityList from './FacilityList';
import { getAssistedLiving } from '../api';

const AssistedLivingList = () => {
  return (
    <FacilityList 
      title="Assisted Living Facilities" 
      kicker="Care Directory"
      subtitle="Browse local assisted living options with a clearer table layout and faster path into each provider record."
      fetchData={getAssistedLiving}
      detailPath="assistedliving"
    />
  );
};

export default AssistedLivingList;
