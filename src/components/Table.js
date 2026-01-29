import { CompactTable } from '@table-library/react-table-library/compact';
import { useTheme } from '@table-library/react-table-library/theme';
import { getTheme } from '@table-library/react-table-library/baseline';
import { useState } from 'react';

export function Table({nodes}){
    let isDataEmpty = false
    if(nodes === undefined && nodes === null && nodes[0] === undefined){
      isDataEmpty = true
    }

    const [columns, ] = useState(isDataEmpty? []:
      Object.keys(nodes[0]).map((key) => ({
        label: key,
        renderCell: ((item) => item[key])
      })));
    
    return (
      <div className='amortization-table'>
        <CompactTable columns={columns} data={{nodes}} theme={useTheme(getTheme())} 
        />;
      </div>
    )
};