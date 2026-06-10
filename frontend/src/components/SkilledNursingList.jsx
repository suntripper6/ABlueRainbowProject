import React from 'react';
import FacilityList from './FacilityList';
import { getSkilledNursing } from '../api';

const SkilledNursingList = () => {
  return (
    <FacilityList 
      title="Skilled Nursing Facilities" 
      kicker="Care Directory"
      subtitle="Scan available nursing facilities with clearer navigation and stronger hierarchy."
      fetchData={getSkilledNursing}
      detailPath="skillednursing"
    />
  );
};

export default SkilledNursingList;
