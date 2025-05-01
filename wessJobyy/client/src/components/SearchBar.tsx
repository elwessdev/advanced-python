import { useState } from 'react';
import { Search } from 'lucide-react';

interface SearchBarProps {
  onSearch: (query: string) => void;
}

const SearchBar = ({ onSearch }: SearchBarProps) => {
  const [query, setQuery] = useState('');
  
  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(query);
  };
  
  return (
    <form onSubmit={handleSearch} className="flex w-full max-w-3xl gap-2">
      <div className="relative flex-1">
        <input
          type="text"
          placeholder="Enter your job"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="w-full px-4 py-3 rounded-full border-2 border-purple-400/30 focus:border-purple-500 focus:outline-none focus:ring-2 focus:ring-purple-500/20 transition-all bg-white/80 backdrop-blur-sm text-slate-800"
        />
      </div>
      <button 
        type="submit" 
        className="bg-gradient-to-r from-purple-400 to-cyan-400 hover:from-cyan-400 hover:to-purple-400 text-white px-6 py-3 rounded-full font-medium shadow-md hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200 flex items-center justify-center"
      >
        <Search className="h-5 w-5 mr-1" />
        Search
      </button>
      {/* <button 
        type="button"
        className="bg-white text-slate-800 border-2 border-gray-200 px-6 py-3 rounded-full font-medium shadow-md hover:shadow-lg hover:border-purple-400/50 transform hover:-translate-y-0.5 transition-all duration-200"
      >
        Export CVS
      </button> */}
    </form>
  );
};

export default SearchBar;