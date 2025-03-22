USE [ESG]
GO

/****** Object:  Table [esg].[framework_modules]    Script Date: 3/22/2025 7:29:02 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [esg].[framework_modules](
	[framework_module_id] [int] NOT NULL,
	[framework_name] [int] NOT NULL,
	[framework_module_name] [nvarchar](200) NOT NULL,
	[framework_module_desc] [nvarchar](max) NOT NULL,
	[module_launch_date] [date] NULL,
	[ts] [datetime2](7) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

