
interface props {
  title: string;
  date: string;
  company: string;
  description: string;
  location: string;
  workType: string;
  link: string;
}

const JobCard = ({title,date,company,location,workType,description,link}:props)=> {
  return (
    <div className="bg-gradient-to-br from-white via-white to-gray-100/30 rounded-3xl p-6 shadow-lg hover:shadow-xl transition-all border border-gray-200/40 group">
      <div className="flex justify-between">
        <div className="space-y-2">
          <h3 className="text-xl font-bold text-slate-800">
            {title} - <span className="text-sm font-medium text-gray-500">{location}</span>
          </h3>
          <p className="text-lg font-medium text-slate-800">{company}</p>
          <p className="text-lg font-medium text-slate-800">{workType}</p>
          <p className="text-gray-500 line-clamp-2">{description}</p>
        </div>
        <div className="flex flex-col items-end justify-between w-[150px]">
          <span className="text-purple-400">{date}</span>
          <a href={link} target="_blank" className="px-5 py-2 rounded-full bg-white border border-purple-400/30 text-purple-500 hover:bg-purple-500 hover:text-white transition-colors duration-300 mt-4 group-hover:scale-105 transform">
            View
          </a>
        </div>
      </div>
    </div>
  );
};

export default JobCard;