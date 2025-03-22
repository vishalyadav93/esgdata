USE [ESG]
GO

/****** Object:  Table [esg].[framework]    Script Date: 3/22/2025 7:28:31 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [esg].[framework](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[framework_name] [varchar](500) NULL,
	[short_name] [varchar](20) NULL,
	[country] [varchar](50) NULL,
	[creation_date] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [esg].[framework] ADD  DEFAULT (getdate()) FOR [creation_date]
GO

